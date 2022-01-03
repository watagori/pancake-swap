from decimal import Decimal
from src.transaction import Transaction

WETH_CONTRACT_ADDRESS = '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'
WETH_DEPOSIT_TOPIC = '0xe1fffcc4923d04b559f4d29a8bfc6cda04eb5b0d3c460751c2402c5c5cc9109c'
WETH_WITHDRAWAL_TOPIC = '0x7fcf532c15f0a6db0bd6d0e038bea71d30d808c7d98cb3bf7268a95bf5081b65'

ERC20_TRANSFER_TOPIC = '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
ERC20_APPROVE_TOPIC = '0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925'

CAKE_CONTRACT_ADDRESS = '0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82'
WBNB_CONTRACT_ADDRESS = '0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c'

PANCAKE_ROUTER_V2_ADDRESS = "0x10ed43c718714eb63d5aa57b78b54704e256024e"
PANCAKE_LP_ADDRESS = "0x0ed7e52944161450477ee417de9cd3a859b14fd0"

WEI = 1000000000000000000


CONTRACT_TYPE = {
    WBNB_CONTRACT_ADDRESS: 'BNB',
    CAKE_CONTRACT_ADDRESS: 'CAKE',
}


class Logs:

    def __init__(self):
        pass

    def get_swap_type(self, receipt):
        if receipt["to"].lower() == PANCAKE_ROUTER_V2_ADDRESS:
            return "bnb_pancakeswap"

        return "unknown"

    def get_transaction_type(self, receipt):
        if len(receipt["logs"]) == 0:
            return "transfer"

        if len(receipt["logs"]) == 1 and receipt["logs"][0]["topics"][0] == ERC20_APPROVE_TOPIC:
            # approve fee
            return "approve"

        if receipt["logs"][0]['topics'][0] == ERC20_APPROVE_TOPIC and len(receipt["logs"]) != 1:
            # remove liquidity
            return "remove-liquidity"

        if receipt["logs"][0]['topics'][0] == ERC20_TRANSFER_TOPIC and \
                receipt["logs"][2]['topics'][0] == ERC20_TRANSFER_TOPIC or \
            receipt["logs"][0]['topics'][0] == WETH_DEPOSIT_TOPIC:
            # exchange
            return "exchange"

        if receipt["logs"][0]['topics'][0] == ERC20_TRANSFER_TOPIC and \
                receipt["logs"][2]['topics'][0] == WETH_DEPOSIT_TOPIC:
            # add liquidity
            return "add-liquidity"

        return "unknown"

    def get_transaction_from(self, receipt):
        credit_from = receipt["from"].lower()
        return credit_from

    def get_transaction_to(self, receipt):
        credit_to = receipt["to"].lower()
        return credit_to

    def get_exchange_contract_address_from(self, receipt):
        token_address_from = receipt["logs"][0]["address"].lower()
        return token_address_from

    def get_exchange_contract_address_to(self, receipt):
        token_address_to = receipt["logs"][2]["address"].lower()
        return token_address_to

    def get_exchange_credit_amount_from(self, receipt):
        credit_amount_from = Decimal(
            int(receipt["logs"][0]["data"].lower(), 16))/Decimal(WEI)
        return str(credit_amount_from)

    def get_exchange_credit_amount_to(self, receipt):
        credit_amount_to = Decimal(
            int(receipt["logs"][2]["data"].lower(), 16))/Decimal(WEI)
        return str(credit_amount_to)

    def get_liquidity_add_contract_address_debit(self, receipt):
        token_address = receipt["logs"][5]["address"].lower()
        return token_address

    def get_liquidity_add_contract_address_credit(self, receipt):
        token_address_one = receipt["logs"][0]["address"].lower()
        token_address_two = receipt["logs"][2]["address"].lower()
        return {token_address_one, token_address_two}

    def get_liquidity_add_amount_debit(self, receipt):
        credit_amount = Decimal(
            int(receipt["logs"][5]["data"].lower(), 16))/Decimal(WEI)
        return str(credit_amount)

    def get_liquidity_add_amount_credit(self, receipt):
        debit_amount_one = Decimal(
            int(receipt["logs"][0]["data"].lower(), 16))/Decimal(WEI)
        debit_amount_two = Decimal(
            int(receipt["logs"][2]["data"].lower(), 16))/Decimal(WEI)
        return {str(debit_amount_one), str(debit_amount_two)}

    def get_liquidity_remove_contract_address_debit(self, receipt):
        token_address_one = receipt["logs"][8]["address"].lower()
        token_address_two = receipt["logs"][9]["address"].lower()
        return {token_address_one, token_address_two}

    def get_liquidity_remove_contract_address_credit(self, receipt):
        token_address = receipt["logs"][0]["address"].lower()
        return token_address

    def get_liquidity_remove_amount_debit(self, receipt):
        debit_amount_one = Decimal(
            int(receipt["logs"][8]["data"].lower(), 16))/Decimal(WEI)
        debit_amount_two = Decimal(
            int(receipt["logs"][9]["data"].lower(), 16))/Decimal(WEI)
        return {str(debit_amount_one), str(debit_amount_two)}

    def get_liquidity_remove_amount_credit(self, receipt):
        credit_amount = Decimal(
            int(receipt["logs"][0]["data"].lower(), 16))/Decimal(WEI)
        return str(credit_amount)

    def get_transaction_fee_from(self, receipt):
        fee_from = receipt["from"].lower()
        return fee_from

    def get_transaction_fee_to(self):
        fee_to = "0x0000000000000000000000000000000000000000"
        return fee_to

    def get_transaction_exchange_detail(self, receipt, transaction_overview):
        caaj_data = {
            "time": Transaction().get_time(transaction_overview),
            "platform": self.get_swap_type(receipt),
            "transaction_hash": Transaction().get_hash(transaction_overview),
            "debit_title": "SPOT",
            "debit_amount": {CONTRACT_TYPE[self.get_exchange_contract_address_to(receipt)]:
                             self.get_exchange_credit_amount_to(receipt)},
            "debit_from": self.get_transaction_to(receipt),
            "debit_to": self.get_transaction_from(receipt),
            "credit_title": "SPOT",
            "credit_amount": {CONTRACT_TYPE[self.get_exchange_contract_address_from(receipt)]:
                              self.get_exchange_credit_amount_from(receipt)},
            "credit_from": self.get_transaction_from(receipt),
            "credit_to": self.get_transaction_to(receipt),
        }

        return caaj_data