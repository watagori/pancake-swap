from src.transaction import Transaction
from src.header import Header

PANCAKE_ADDRESS = ["0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82",
                   "0x10ed43c718714eb63d5aa57b78b54704e256024e"]


class CaajConverter():
    def __init__(self, header_data, receipt_data):
        self.header_data = header_data
        self.receipt_data = receipt_data

    def get_caaj(self):
        swap_type = Header(self.header_data).get_transaction_to()
        if swap_type in PANCAKE_ADDRESS:
            caaj_data = Transaction(
                self.header_data, self.receipt_data).get_caaj()
            caaj_data_fee = Transaction(
                self.header_data, self.receipt_data).get_caaj_fee()
            return [caaj_data, caaj_data_fee]
        else:
            pass
