from datetime import datetime
from decimal import Decimal

WEI = 1000000000000000000


class Transaction:
    def __init__(self):
        pass

    def get_hash(self, transaction):
        return transaction['hash']

    def get_time(self, transaction):
        timestamp = transaction['timeStamp']
        time = datetime.fromtimestamp(
            int(timestamp)).strftime('%Y-%m-%d-%H:%M:%S')
        return time

    def get_transaction_fee(self, transaction):
        fee = Decimal(transaction['gasPrice']) * \
            Decimal(transaction['gasUsed'])/Decimal(WEI)
        return str(fee)
