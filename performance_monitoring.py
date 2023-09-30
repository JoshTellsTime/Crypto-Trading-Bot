```python
import time
from bot_deployment import BotDeployment

class PerformanceMonitoring:
    def __init__(self, bot: BotDeployment, monitoring_interval: int):
        self.bot = bot
        self.monitoring_interval = monitoring_interval

    def monitor_performance(self):
        while True:
            # Get the current portfolio
            portfolio = self.bot.strategy.get_portfolio()

            # Calculate the total value of the portfolio
            total_value = sum([coin['amount'] * coin['price'] for coin in portfolio])

            # Print the total value of the portfolio
            print(f"Total portfolio value at {time.ctime()}: {total_value}")

            # Sleep for the monitoring interval
            time.sleep(self.monitoring_interval)

if __name__ == "__main__":
    bot = BotDeployment('model.h5', 'https://api.binance.com', 'YOUR_API_KEY', 'BTCUSDT', 0.02, 0.05)
    monitor = PerformanceMonitoring(bot, 60)
    monitor.monitor_performance()
```
