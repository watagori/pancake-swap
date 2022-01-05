'''Get logs json data of the transaciton by any address'''
import json
from web3 import Web3
import certifi
import requests

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
ORDER = "ASC"


# Don't change the code below
BSC_URL = "https://bsc-dataseed.binance.org/"
w3 = Web3(Web3.HTTPProvider(BSC_URL))


def get_logs_by_address(transaction_id, filename):
    '''Get transaction by address'''
    bsc_receipt = w3.eth.get_transaction_receipt(transaction_id)

    jsondata = Web3.toJSON(bsc_receipt)
    jsonfile = open("data/receipt/" + filename + ".json",
                    "w", encoding="utf-8")
    jsonfile.write(jsondata)
    jsonfile.close()


def get_transaction(transaction_number, address):
    url = "https://api.bscscan.com/api?module=account&action=txlist&address=" + \
        address + "&startblock=0&endblock=99999999&page=1&offset=" + str(transaction_number) \
        + "&sort=" + ORDER + "&apikey = TBY4C25PY394RSWTF6DUXWCHJTYF8Q8H1U"
    response = requests.get(url, verify=certifi.where())
    address_content = response.json()
    details = address_content.get("result")

    for index, transaction in enumerate(details):
        with open("data/header/" + FILENAME[index] + ".json", "w", encoding="utf-8") \
                as outfile:
            json.dump(transaction, outfile)

        get_logs_by_address(transaction['hash'], FILENAME[index])


get_transaction(TRANSACTION_NUMBER, ADDRESS)
