```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from sklearn.model_selection import train_test_split
import numpy as np

class ModelTrainer:
    def __init__(self, input_shape, output_shape):
        self.model = self.build_model(input_shape, output_shape)

    def build_model(self, input_shape, output_shape):
        model = Sequential()
        model.add(LSTM(50, return_sequences=True, input_shape=input_shape))
        model.add(Dropout(0.2))
        model.add(LSTM(50, return_sequences=False))
        model.add(Dropout(0.2))
        model.add(Dense(25))
        model.add(Dense(output_shape))

        model.compile(optimizer='adam', loss='mean_squared_error')
        return model

    def train_model(self, X, y, epochs=5, batch_size=64, validation_split=0.2):
        checkpoint = ModelCheckpoint('model.h5', save_best_only=True, monitor='val_loss', mode='min')
        stop = EarlyStopping(monitor='val_loss', patience=5, mode='min')

        self.model.fit(X, y, batch_size=batch_size, epochs=epochs, validation_split=validation_split, callbacks=[checkpoint, stop])

    def load_model(self, model_path):
        self.model = tf.keras.models.load_model(model_path)

if __name__ == "__main__":
    from data_collection import DataCollector
    from data_preprocessing import DataPreprocessor

    collector = DataCollector('https://api.binance.com', 'YOUR_API_KEY')
    historical_data = collector.get_historical_data('BTCUSDT', '1d', int(time.mktime(datetime(2020, 1, 1).timetuple()))*1000, int(time.mktime(datetime(2022, 1, 1).timetuple()))*1000)

    preprocessor = DataPreprocessor()
    preprocessed_data = preprocessor.preprocess_data(historical_data)

    X = np.array(preprocessed_data.iloc[:-1])
    y = np.array(preprocessed_data.iloc[1:])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    trainer = ModelTrainer((X_train.shape[1], 1), y_train.shape[1])
    trainer.train_model(X_train, y_train)
```
