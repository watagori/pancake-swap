import csv
import json
from caaj_plugin.caaj_plugin import CaajPlugin
from src.transaction import Transaction
from src.header import Header


PANCAKE_ADDRESS = ["0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82",
                   "0x10ed43c718714eb63d5aa57b78b54704e256024e"]


class PancakePlugin(CaajPlugin):
    def __init__(self, header_data, receipt_data):
        self.header_data = header_data
        self.receipt_data = receipt_data
a
    def get_caajs(self, transaction: json, subject_address: str):
        swap_type = Header(self.header_data).get_transaction_to()
        if swap_type in PANCAKE_ADDRESS:
            caaj_data = Transaction(
                self.header_data, self.receipt_data).get_caaj()
            caaj_data_fee = Transaction(
                self.header_data, self.receipt_data).get_caaj_fee()

            WriteCaaj(caaj_data).write_caaj()
            WriteCaaj(caaj_data_fee).write_caaj()

            return [caaj_data, caaj_data_fee]
        else:
            pass

    def can_handle(self, transaction):
        pass


class WriteCaaj():
    def __init__(self, data):
        self.time = data['time']
        self.platform = data['platfrom']
        self.transaction_id = data['transaction_id']
        self.debit_title = data['debit_title']
        self.debit_amount = data['debit_amount']
        self.debit_from = data['debit_from']
        self.debit_to = data['debit_to']
        self.credit_title = data['credit_title']
        self.credit_amount = data['credit_amount']
        self.credit_from = data['credit_from']
        self.credit_to = data['credit_to']
        self.comment = data['comment']

    def write_caaj(self):
        caaj_csv = open("data/caaj/pancake.csv", "a", encoding="utf-8")
        writer = csv.writer(caaj_csv)
        writer.writerow([
            self.time, self.platform, self.transaction_id, self.debit_title,
            self.debit_amount, self.debit_from, self.debit_to,
            self.credit_title, self.credit_amount, self.credit_from,
            self.credit_to, self.comment]
        )
        caaj_csv.close()
