'''Get logs json data of the transaciton by any address'''
# from decimal import Decimal
# from datetime import datetime
from web3 import Web3
import certifi
import requests
import json

# transaction history
# transafer(waki -> nishi) 0x57932a25175a1184d433be880655d1ee6d1a9e62853723e695f1d38553914462
# exchange(BNB -> CAKE) 0x4f8534e85849cb54f0ae4ca0718939ab22de248f64e2e4dc607a76b12f20f109
# CAKE max approve 0x36512c7e09e3570dfc53176252678ee9617660550d36f4da797afba6fc55bba6
# liquidity(BNB + CAKE -> LP) 0xb4c3ed5db127089cd1be4b247537d163e74e99e33598348579ffae4f81877834
# liquidity(LP -> BNB + CAKE) 0xdc70901bcb2517a885e41ab9ccb0a739ae73af4b8862a1c46f9ca2ce583b8cd3
# exchange(CAKE -> BNB) 0xd3f63cdad3bb1b8ea46fafbaac21c93cdb7204daece60f1a44aaa198f58371fa

TRANSACTION_ID = "0x57932a25175a1184d433be880655d1ee6d1a9e62853723e695f1d38553914462"
BSC_URL = "https://bsc-dataseed.binance.org/"
w3 = Web3(Web3.HTTPProvider(BSC_URL))


def get_logs_by_address(transaction_id):
    '''Get transaction by address'''
    bsc_receipt = w3.eth.get_transaction_receipt(transaction_id)

    jsondata = Web3.toJSON(bsc_receipt["logs"])
    jsonfile = open("data/logs/transfer_waki_to_nishi.json",
                    "w", encoding="utf-8")
    jsonfile.write(jsondata)
    jsonfile.close()


get_logs_by_address(TRANSACTION_ID)


def get_transaction(transaction_number, address):
    url = "https://api.bscscan.com/api?module=account&action=txlist&address=" + address \
        + "&startblock=0&endblock=99999999&page=1&offset=" + str(transaction_number) \
        + "&sort=desc&apikey=TBY4C25PY394RSWTF6DUXWCHJTYF8Q8H1U"
    response = requests.get(url, verify=certifi.where())
    address_content = response.json()
    details = address_content.get("result")

    for index, transaction in enumerate(details):

        with open("data/transaction/transaction" + str(index) + ".json", "w", encoding="utf-8") as outfile:
            json.dump(transaction, outfile)


get_transaction(
    5, "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E")
