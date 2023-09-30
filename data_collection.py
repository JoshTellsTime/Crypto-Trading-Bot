```python
import requests
import pandas as pd
from datetime import datetime
import time

class DataCollector:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def get_historical_data(self, symbol, interval, start_time, end_time):
        url = f"{self.base_url}/api/v3/klines"
        headers = {
            'X-MBX-APIKEY': self.api_key
        }
        params = {
            'symbol': symbol,
            'interval': interval,
            'startTime': start_time,
            'endTime': end_time
        }
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        df = pd.DataFrame(data)
        df.columns = ['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore']
        df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
        df['close_time'] = pd.to_datetime(df['close_time'], unit='ms')
        return df

    def get_realtime_data(self, symbol):
        url = f"{self.base_url}/api/v3/ticker/price"
        headers = {
            'X-MBX-APIKEY': self.api_key
        }
        params = {
            'symbol': symbol
        }
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        return data

if __name__ == "__main__":
    collector = DataCollector('https://api.binance.com', 'YOUR_API_KEY')
    historical_data = collector.get_historical_data('BTCUSDT', '1d', int(time.mktime(datetime(2020, 1, 1).timetuple()))*1000, int(time.mktime(datetime(2022, 1, 1).timetuple()))*1000)
    print(historical_data)
    realtime_data = collector.get_realtime_data('BTCUSDT')
    print(realtime_data)
```
