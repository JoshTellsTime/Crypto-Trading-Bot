```python
import requests
import json

class APIIntegration:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            'X-MBX-APIKEY': self.api_key,
            'Content-Type': 'application/json'
        }

    def place_order(self, symbol, side, order_type, quantity):
        url = f"{self.base_url}/api/v3/order"
        params = {
            'symbol': symbol,
            'side': side,
            'type': order_type,
            'quantity': quantity
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(params))
        return response.json()

    def get_order(self, symbol, orderId):
        url = f"{self.base_url}/api/v3/order"
        params = {
            'symbol': symbol,
            'orderId': orderId
        }
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def cancel_order(self, symbol, orderId):
        url = f"{self.base_url}/api/v3/order"
        params = {
            'symbol': symbol,
            'orderId': orderId
        }
        response = requests.delete(url, headers=self.headers, params=params)
        return response.json()

    def get_account_info(self):
        url = f"{self.base_url}/api/v3/account"
        response = requests.get(url, headers=self.headers)
        return response.json()

if __name__ == "__main__":
    api = APIIntegration('https://api.binance.com', 'YOUR_API_KEY')
    order = api.place_order('BTCUSDT', 'BUY', 'MARKET', 0.001)
    print(order)
    order_info = api.get_order('BTCUSDT', order['orderId'])
    print(order_info)
    account_info = api.get_account_info()
    print(account_info)
```
