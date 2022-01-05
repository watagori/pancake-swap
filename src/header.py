"""Get timestamp and transaction fee from the header of BSCScan"""
from datetime import datetime
from decimal import Decimal

WEI = 1000000000000000000


class Header(object):
    def __init__(self, header):
        self.timestamp = header['timeStamp']
        self.gas_price = header['gasPrice']
        self.gas_used = header['gasUsed']
        self.fee_from = header['from']
        self.transaction_hash = header['hash']

    def get_time(self):
        time = datetime.fromtimestamp(
            int(self.timestamp)).strftime('%Y-%m-%d-%H:%M:%S')
        return time

    def get_transaction_fee(self):
        transaction_fee = str(Decimal(
            self.gas_price) * Decimal(self.gas_used)/Decimal(WEI))
        return transaction_fee

    def get_fee_from(self):
        fee_from = self.fee_from
        return fee_from

    def get_transaction_hash(self):
        transaction_hash = self.transaction_hash
        return transaction_hash
