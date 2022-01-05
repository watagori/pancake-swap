from src.header import Header
from src.evm_receipt import EvmReceipt


CAKE_CONTRACT_ADDRESS = '0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82'
WBNB_CONTRACT_ADDRESS = '0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c'

token_type = {
    CAKE_CONTRACT_ADDRESS: "CAKE",
    WBNB_CONTRACT_ADDRESS: "BNB",
}


class Transaction():
    def __init__(self, header_data, receipt_data):
        self.header_data = header_data
        self.receipt_data = receipt_data

    def get_caaj(self):
        if EvmReceipt(self.receipt_data).get_result()['type'] == 'exchange':
            caaj_data = {
                "time": Header(self.header_data).get_time(),
                "platfrom": "bnb_pancakeswap",
                "transaction_id": Header(self.header_data).get_transaction_hash(),
                "debit_title": "SPOT",
                "debit_amount": {token_type
                                 [EvmReceipt(self.receipt_data).get_result()[
                                     'to_token_address']]:
                                 EvmReceipt(self.receipt_data).get_result()['to_token_amount']},
                "debit_from": EvmReceipt(self.receipt_data).get_result()['to_address'],
                "debit_to": EvmReceipt(self.receipt_data).get_result()['from_address'],
                "credit_title": "SPOT",
                "credit_amount": {token_type
                                  [EvmReceipt(self.receipt_data).get_result()[
                                      'from_token_address']]:
                                  EvmReceipt(self.receipt_data).get_result()['from_token_amount']},
                "credit_from": EvmReceipt(self.receipt_data).get_result()['from_address'],
                "credit_to": EvmReceipt(self.receipt_data).get_result()['to_address'],
                "comment": "pancakeswap trade"

            }
            return caaj_data

        elif EvmReceipt(self.receipt_data).get_result()['type'] == "add_liquidity":
            caaj_data = {
                "time": Header(self.header_data).get_time(),
                "platfrom": "bnb_pancakeswap",
                "transaction_id": Header(self.header_data).get_transaction_hash(),
                "debit_title": "LIQUIDITY",
                "debit_amount": {
                    EvmReceipt(self.receipt_data).get_result()[
                        'to_token_address']:
                    EvmReceipt(self.receipt_data).get_result()['to_token_amount']},
                "debit_from": EvmReceipt(self.receipt_data).get_result()['to_address'],
                "debit_to": EvmReceipt(self.receipt_data).get_result()['from_address'],
                "credit_title": "SPOT",
                "credit_amount": {token_type[list(EvmReceipt(self.receipt_data)
                                                  .get_result()[
                    'from_token_address'])[0]]: list(EvmReceipt(self.receipt_data)
                                                     .get_result()['from_token_amount'])[0],
                    token_type[list(EvmReceipt(self.receipt_data).get_result()[
                        'from_token_address'])[1]]: list(EvmReceipt(self.receipt_data)
                                                         .get_result()['from_token_amount'])[1]},
                "credit_from": EvmReceipt(self.receipt_data).get_result()['from_address'],
                "credit_to": EvmReceipt(self.receipt_data).get_result()['to_address'],
                "comment": "pancakeswap add liquidity"
            }
            return caaj_data

        elif EvmReceipt(self.receipt_data).get_result()['type'] == "remove_liquidity":
            caaj_data = {
                "time": Header(self.header_data).get_time(),
                "platfrom": "bnb_pancakeswap",
                "transaction_id": Header(self.header_data).get_transaction_hash(),
                "debit_title": "SPOT",
                "debit_amount": {token_type[
                    list(EvmReceipt(self.receipt_data)
                         .get_result()['to_token_address'])[0]]:
                    list(EvmReceipt(self.receipt_data)
                         .get_result()['to_token_amount'])[0],
                    token_type[list(EvmReceipt(self.receipt_data).get_result()[
                        'to_token_address'])[1]]: list(EvmReceipt(self.receipt_data)
                                                       .get_result()['to_token_amount'])[1]},
                "debit_from": EvmReceipt(self.receipt_data).get_result()['to_address'],
                "debit_to": EvmReceipt(self.receipt_data).get_result()['from_address'],
                "credit_title": "LIQUIDITY",
                "credit_amount":  {
                    EvmReceipt(self.receipt_data).get_result()[
                        'from_token_address']:
                    EvmReceipt(self.receipt_data).get_result()['from_token_amount']},
                "credit_from": EvmReceipt(self.receipt_data).get_result()['from_address'],
                "credit_to": EvmReceipt(self.receipt_data).get_result()['to_address'],
                "comment": "pancakeswap remove liquidity"
            }
            return caaj_data

    def get_caaj_fee(self):
        caaj_data = {
            "time": Header(self.header_data).get_time(),
            "platfrom": "bnb_pancakeswap",
            "transaction_id": Header(self.header_data).get_transaction_hash(),
            "debit_title": "SPOT",
            "debit_amount": {"BNB": Header(self.header_data).get_transaction_fee()},
            "debit_from": "0x0000000000000000000000000000000000000000",
            "debit_to": EvmReceipt(self.receipt_data).get_result()['from_address'],
            "credit_title": "SPOT",
            "credit_amount": {"BNB": Header(self.header_data).get_transaction_fee()},
            "credit_from": EvmReceipt(self.receipt_data).get_result()['from_address'],
            "credit_to": "0x0000000000000000000000000000000000000000",
            "comment": "pancakeswap fee"

        }
        return caaj_data
