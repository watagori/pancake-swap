"""Get type,to,from ,amout of transaction from EVM logs"""
from decimal import Decimal


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


class EvmReceipt:
    def __init__(self, logs, from_address, to_address):
        self.logs = logs
        self.from_address = from_address
        self.to_address = to_address

    def get_transaction_type(self):
        """Get type of transaction from EVM logs"""
        if len(self.logs) == 0:
            return "transfer"

        elif len(self.logs) == 1 and self.logs[0]["topics"][0] == ERC20_APPROVE_TOPIC:
            return "approve"

        elif self.logs[0]['topics'][0] == ERC20_TRANSFER_TOPIC and \
                self.logs[2]['topics'][0] == ERC20_TRANSFER_TOPIC or \
                self.logs[0]['topics'][0] == WETH_DEPOSIT_TOPIC:
            return "exchange"

        elif self.logs[0]['topics'][0] == ERC20_TRANSFER_TOPIC and \
                self.logs[2]['topics'][0] == WETH_DEPOSIT_TOPIC:
            return "add-liquidity"

        elif self.logs[0]['topics'][0] == ERC20_APPROVE_TOPIC and \
                len(self.logs) != 1:
            return "remove-liquidity"

        return "unknown"

    def get_from_address(self):
        """Get from address of transaction from EVM logs"""
        from_address = self.from_address.lower()
        return from_address

    def get_to_address(self):
        """Get to address of transaction from EVM logs"""
        to_address = self.to_address.lower()
        return to_address

    def get_exchange_credit_token(self):
        """Get from token address of exchange transaction from EVM logs"""
        token_address = self.logs[0]['address'].lower()
        return token_address

    def get_exchange_debit_token(self):
        """Get to token address of exchange transaction from EVM logs"""
        token_address = self.logs[2]['address'].lower()
        return token_address

    def get_exchange_credit_amount(self):
        """Get credit amount of exchange transaction from EVM logs"""
        credit_amount = str(Decimal(
            int(self.logs[0]["data"].lower(), 16))/Decimal(WEI))
        return credit_amount

    def get_exchange_debit_amount(self):
        """Get debit amount of exchange transaction from EVM logs"""
        debit_amount = str(Decimal(
            int(self.logs[2]["data"].lower(), 16))/Decimal(WEI))
        return debit_amount

    def get_liquidity_add_credit_token(self):
        """Get from token address of liquidity add transaction from EVM logs"""
        token_address_1 = self.logs[0]['address'].lower()
        token_address_2 = self.logs[2]['address'].lower()
        return {token_address_1, token_address_2}

    def get_liquidity_add_debit_token(self):
        """Get to token address of liquidity add transaction from EVM logs"""
        token_address = self.logs[5]['address'].lower()
        return token_address

    def get_liquidity_add_credit_amount(self):
        """Get credit amount of liquidity add transaction from EVM logs"""
        credit_amount_1 = str(Decimal(
            int(self.logs[0]["data"].lower(), 16))/Decimal(WEI))
        credit_amount_2 = str(Decimal(
            int(self.logs[2]["data"].lower(), 16))/Decimal(WEI))
        return {credit_amount_1, credit_amount_2}

    def get_liquidity_add_debit_amount(self):
        """Get debit amount of liquidity add transaction from EVM logs"""
        debit_amount = str(Decimal(
            int(self.logs[5]["data"].lower(), 16))/Decimal(WEI))
        return debit_amount

    def get_liquidity_remove_credit_token(self):
        """Get from token address of liquidity remove transaction from EVM logs"""
        token_address = self.logs[0]['address'].lower()
        return token_address

    def get_liquidity_remove_debit_token(self):
        """Get to token address of liquidity remove transaction from EVM logs"""
        token_address_1 = self.logs[8]['address'].lower()
        token_address_2 = self.logs[9]['address'].lower()
        return {token_address_1, token_address_2}

    def get_liquidity_remove_credit_amount(self):
        """Get credit amount of liquidity remove transaction from EVM logs"""
        credit_amount = str(Decimal(
            int(self.logs[0]["data"].lower(), 16))/Decimal(WEI))
        return credit_amount

    def get_liquidity_remove_debit_amount(self):
        """Get debit amount of liquidity remove transaction from EVM logs"""
        debit_amount_1 = str(Decimal(
            int(self.logs[8]["data"].lower(), 16))/Decimal(WEI))
        debit_amount_2 = str(Decimal(
            int(self.logs[9]["data"].lower(), 16))/Decimal(WEI))
        return {debit_amount_1, debit_amount_2}
