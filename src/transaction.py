from src.header import Header
from src.evm_receipt import EvmReceipt

WETH_CONTRACT_ADDRESS = '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'
WETH_DEPOSIT_TOPIC = '0xe1fffcc4923d04b559f4d29a8bfc6cda04eb5b0d3c460751c2402c5c5cc9109c'
WETH_WITHDRAWAL_TOPIC = '0x7fcf532c15f0a6db0bd6d0e038bea71d30d808c7d98cb3bf7268a95bf5081b65'

ERC20_TRANSFER_TOPIC = '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
ERC20_APPROVE_TOPIC = '0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925'

CAKE_CONTRACT_ADDRESS = '0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82'
WBNB_CONTRACT_ADDRESS = '0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c'

PANCAKE_ROUTER_V2_ADDRESS = "0x10ed43c718714eb63d5aa57b78b54704e256024e"
PANCAKE_LP_ADDRESS = "0x0ed7e52944161450477ee417de9cd3a859b14fd0"

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
