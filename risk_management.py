```python
class RiskManagement:
    def __init__(self, stop_loss, take_profit):
        self.stop_loss = stop_loss
        self.take_profit = take_profit

    def check_risk(self, current_price, bought_price):
        # Calculate the profit or loss
        profit_or_loss = (current_price - bought_price) / bought_price

        # Check if the stop loss or take profit has been hit
        if profit_or_loss <= -self.stop_loss:
            return 'sell'
        elif profit_or_loss >= self.take_profit:
            return 'sell'
        else:
            return 'hold'

if __name__ == "__main__":
    risk_management = RiskManagement(0.05, 0.1)  # 5% stop loss, 10% take profit
    action = risk_management.check_risk(10000, 10500)  # Current price, bought price
    print(action)
```
