WETH_CONTRACT_ADDRESS = '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'
WETH_DEPOSIT_TOPIC = '0xe1fffcc4923d04b559f4d29a8bfc6cda04eb5b0d3c460751c2402c5c5cc9109c'
WETH_WITHDRAWAL_TOPIC = '0x7fcf532c15f0a6db0bd6d0e038bea71d30d808c7d98cb3bf7268a95bf5081b65'

ERC20_TRANSFER_TOPIC = '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
ERC20_APPROVE_TOPIC = '0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925'

CAKE_CONTRACT_ADDRESS = '0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82'
WBNB_CONTRACT_ADDRESS = '0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c'

PANCAKE_ROUTER_V2_ADDRESS = "0x10ed43c718714eb63d5aa57b78b54704e256024e"
PANCAKE_LP_ADDRESS = "0x0ed7e52944161450477ee417de9cd3a859b14fd0"


class Logs:

    def __init__(self):
        pass

    def get_transaction_type(self, receipt):
        if len(receipt["logs"]) == 0:
            return "transfer"

        if len(receipt["logs"]) == 1 and receipt["logs"][0]["topics"][0] == ERC20_APPROVE_TOPIC:
            # approve fee
            return "approve"

        if receipt["logs"][0]['topics'][0] == WETH_DEPOSIT_TOPIC:
            # exchange(BNB -> other)
            return "exchange-bnb"

        if receipt["logs"][0]['topics'][0] == ERC20_APPROVE_TOPIC and len(receipt["logs"]) != 1:
            # remove liquidity
            return "remove-liquidity"

        if receipt["logs"][0]['topics'][0] == ERC20_TRANSFER_TOPIC and \
                receipt["logs"][2]['topics'][0] == ERC20_TRANSFER_TOPIC:
            # exchange(non-BNB -> non-BNB)
            return "exchange"

        if receipt["logs"][0]['topics'][0] == ERC20_TRANSFER_TOPIC and \
                receipt["logs"][2]['topics'][0] == WETH_DEPOSIT_TOPIC:
            # add liquidity
            return "add-liquidity"

    def get_transfer_from(self, receipt):
        credit_from = receipt["from"].lower()
        return credit_from

    def get_transfer_to(self, receipt):
        credit_to = receipt["to"].lower()
        return credit_to
