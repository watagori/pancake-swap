"""Get timestamp and transaction fee from the header of a block."""
from datetime import datetime
from decimal import Decimal

WEI = 1000000000000000000


class Header:
    def __init__(self, timestamp, gas_price, gas_used):
        self.timestamp = timestamp
        self.gas_price = gas_price
        self.gas_used = gas_used

    def get_time(self):
        time = datetime.fromtimestamp(
            int(self.timestamp)).strftime('%Y-%m-%d-%H:%M:%S')
        return time

    def get_transaction_fee(self):
        transaction_fee = str(Decimal(
            self.gas_price) * Decimal(self.gas_used)/Decimal(WEI))
        return transaction_fee
