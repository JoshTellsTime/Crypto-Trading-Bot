```python
import hashlib
import hmac
import time
import requests

class Security:
    def __init__(self, base_url, api_key, secret_key):
        self.base_url = base_url
        self.api_key = api_key
        self.secret_key = secret_key

    def get_signature(self, params: dict):
        ordered_params = {k: v for k, v in sorted(params.items())}
        query_string = '&'.join(["{}={}".format(d, ordered_params[d]) for d in ordered_params])
        return hmac.new(self.secret_key.encode(), query_string.encode(), hashlib.sha256).hexdigest()

    def secure_request(self, endpoint: str, params: dict = {}):
        headers = {
            'X-MBX-APIKEY': self.api_key
        }

        params['timestamp'] = int(time.time() * 1000)
        params['signature'] = self.get_signature(params)

        url = self.base_url + endpoint
        response = requests.get(url, headers=headers, params=params)

        if response.status_code != 200:
            raise Exception(f"Request failed with error {response.status_code}: {response.text}")

        return response.json()

if __name__ == "__main__":
    security = Security('https://api.binance.com', 'YOUR_API_KEY', 'YOUR_SECRET_KEY')
    print(security.secure_request('/api/v3/account'))
```
