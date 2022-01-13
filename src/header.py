"""Get timestamp and transaction fee from the header of BSCScan"""
from datetime import datetime
from decimal import Decimal


WEI = 1000000000000000000


class Header(object):

    def __init__(self, header):
        self.header = header

    def get_time(self):
        time = datetime.fromtimestamp(
            int(self.header['timeStamp'])).strftime('%Y-%m-%d-%H:%M:%S')
        return time

    def get_transaction_fee(self):
        transaction_fee = str(Decimal(
            self.header['gasPrice']) * Decimal(self.header['gasUsed'])/Decimal(WEI))
        return transaction_fee

    def get_transaction_from(self):
        transaction_from = self.header['from']
        return transaction_from

    def get_transaction_hash(self):
        transaction_hash = self.header['hash']
        return transaction_hash

    def get_transaction_to(self):
        transaction_to = self.header['to']
        return transaction_to
