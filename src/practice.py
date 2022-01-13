import json
from web3 import Web3
import certifi
import requests
from web3.middleware import geth_poa_middleware

# change to your own settings
FILENAME = [
    "transfer",
    "exchange_bnb_to_cake",
    "approve",
    "liquidity_bnb_and_cake_to_lp",
    "liquidity_lp_to_bnb_and_cake",
    "exchange_cake_to_bnb"
]
TRANSACTION_NUMBER = 6
ADDRESS = "0xda28ecfc40181a6dad8b52723035dfba3386d26e"
ORDER = "asc"


# Don't change the code below
BSC_URL = "https://bsc-dataseed.binance.org/"
w3 = Web3(Web3.HTTPProvider(BSC_URL))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)


def get_block():
    block = w3.eth.get_block(13856363, full_transactions=True)
    block_json = w3.toJSON(block)
    jsonfile = open("block.json",
                    "w", encoding="utf-8")
    jsonfile.write(block_json)
    jsonfile.close()


get_block()
