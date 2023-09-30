```python
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

class DataPreprocessor:
    def __init__(self):
        self.scaler = MinMaxScaler()

    def preprocess_data(self, df):
        # Drop unnecessary columns
        df = df.drop(['open_time', 'close_time', 'ignore'], axis=1)

        # Convert data types to float
        for column in df.columns:
            df[column] = df[column].astype(float)

        # Normalize the data
        df_scaled = pd.DataFrame(self.scaler.fit_transform(df), columns=df.columns)

        return df_scaled

    def inverse_transform(self, df):
        # Inverse transform the scaled data
        df_inverse = pd.DataFrame(self.scaler.inverse_transform(df), columns=df.columns)

        return df_inverse

if __name__ == "__main__":
    from data_collection import DataCollector

    collector = DataCollector('https://api.binance.com', 'YOUR_API_KEY')
    historical_data = collector.get_historical_data('BTCUSDT', '1d', int(time.mktime(datetime(2020, 1, 1).timetuple()))*1000, int(time.mktime(datetime(2022, 1, 1).timetuple()))*1000)

    preprocessor = DataPreprocessor()
    preprocessed_data = preprocessor.preprocess_data(historical_data)
    print(preprocessed_data)

    inverse_data = preprocessor.inverse_transform(preprocessed_data)
    print(inverse_data)
```
