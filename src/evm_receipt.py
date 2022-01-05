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


class EvmReceipt(object):
    def __init__(self, receipt):
        self.logs = receipt['logs']
        self.from_address = receipt['from']
        self.to_address = receipt['to']

    def get_result(self):
        if len(self.logs) == 0:
            result = {
                'type': 'transfer',
            }
            return result

        elif len(self.logs) == 1 and self.logs[0]["topics"][0] == ERC20_APPROVE_TOPIC:
            # approve
            result = {
                'type': 'approve',
                "from_address": self.from_address.lower(),
                "to_address": self.to_address.lower(),
            }
            return result

        elif self.logs[0]['topics'][0] == ERC20_TRANSFER_TOPIC and\
                self.logs[2]['topics'][0] == ERC20_TRANSFER_TOPIC or\
                self.logs[0]['topics'][0] == WETH_DEPOSIT_TOPIC:
            #  Ecchange
            result = {
                'type': 'exchange',
                "from_address": self.from_address.lower(),
                "to_address": self.to_address.lower(),
                "from_token_address": self.logs[0]['address'].lower(),
                "to_token_address": self.logs[2]['address'].lower(),
                "from_token_amount": str(Decimal(
                    int(self.logs[0]["data"].lower(), 16))/Decimal(WEI)),
                "to_token_amount": str(Decimal(
                    int(self.logs[2]["data"].lower(), 16))/Decimal(WEI)),
            }
            return result

        elif self.logs[0]['topics'][0] == ERC20_TRANSFER_TOPIC and\
                self.logs[2]['topics'][0] == WETH_DEPOSIT_TOPIC:
            # Add liquidity
            result = {
                'type': 'add_liquidity',
                "from_address": self.from_address.lower(),
                "to_address": self.to_address.lower(),
                "from_token_address": {self.logs[0]['address'].lower(),
                                       self.logs[2]['address'].lower()},
                "to_token_address": self.logs[5]['address'].lower(),
                "from_token_amount": {str(Decimal(
                    int(self.logs[2]["data"].lower(), 16))/Decimal(WEI)), str(Decimal(
                        int(self.logs[0]["data"].lower(), 16))/Decimal(WEI))},
                "to_token_amount": str(Decimal(
                    int(self.logs[5]["data"].lower(), 16))/Decimal(WEI)),
            }
            return result

        elif self.logs[0]['topics'][0] == ERC20_APPROVE_TOPIC and\
                len(self.logs) != 1:
            # Remove liquidity
            result = {
                'type': 'remove_liquidity',
                "from_address": self.from_address.lower(),
                "to_address": self.to_address.lower(),
                "to_token_address": {self.logs[8]['address'].lower(),
                                     self.logs[9]['address'].lower()},
                "from_token_address": self.logs[0]['address'].lower(),
                "to_token_amount": {str(Decimal(
                    int(self.logs[8]["data"].lower(), 16))/Decimal(WEI)), str(Decimal(
                        int(self.logs[9]["data"].lower(), 16))/Decimal(WEI))},
                "from_token_amount": str(Decimal(
                    int(self.logs[0]["data"].lower(), 16))/Decimal(WEI)),
            }
            return result

        return "unknown"
