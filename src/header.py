"""Get timestamp and transaction fee from the header of BSCScan"""
from datetime import datetime
from decimal import Decimal

WEI = 1000000000000000000


class Header:
    def __init__(self, timestamp, gas_price, gas_used, fee_from):
        self.timestamp = timestamp
        self.gas_price = gas_price
        self.gas_used = gas_used
        self.fee_from = fee_from

    def get_time(self):
        time = datetime.fromtimestamp(
            int(self.timestamp)).strftime('%Y-%m-%d-%H:%M:%S')
        return time

    def get_transaction_fee(self):
        transaction_fee = str(Decimal(
            self.gas_price) * Decimal(self.gas_used)/Decimal(WEI))
        return transaction_fee

    def get_fee_from(self):
        """Get transaction fee from EVM logs"""
        fee_from = self.fee_from
        return fee_from

    def get_fee_to(self):
        """Get transaction fee to EVM logs"""
        fee_to = "0x0000000000000000000000000000000000000000"
        return fee_to
