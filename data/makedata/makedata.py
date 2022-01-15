'''Get logs json data of the transaciton by any address'''
import imp
import json
from web3 import Web3
import certifi
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# exchange bnb -> cake 0x5e17cf11995ddd7d85043b6916bc25e979834b474483d4faea698a3289a0a3df
# exchange bnb -> busd 0x9a69c209cb52b96efe0d028bbbcdbce9247e62edcd77867ebcf3f3c27869fd3f
# exchange cake -> bnb 0x35079782f862c0c6879de84d3b03221e00be893e8b41341200ef554c65d9c68d
# exchange busd -> bnb 0xbddb26aee13755aac45e4d4a31c19ba89a1ff9436c8ee42fe30164228659619f
# exchange cake -> usdt 0x726ddb54d7d5e40739785a77a3be4267b4ad4ed9bf79c84c737970c406083d14
# exchange(fail) usdt -> busd 0x00c4e3b39507bd07ae453204d9cbf8f2132d83f7dbcacdb198e6f9e9e6557933
# exchange busd -> eth 0x7d3e9e271e044818b6aedd20afb512399d4aad283b7d307158ceac35522b56a7
# add liquidity busd + cake 0xbfa3e15973ebaedebea4386c23a698a5839b77e364896fcf9de87660c9ea98d8
# add liquidity bnb + eth 0x9a69c209cb52b96efe0d028bbbcdbce9247e62edcd77867ebcf3f3c27869fd3f
# remove liquidity bnb + eth 0xcdbcd503fe35fd1da4b630f6fe6f4f18c505a8034d3d3b169ad1e099c60f841e
# remove liquidity cake + busd 0xabcf9d8b9f5b1d46bab05de14a63db964ecdf1a13cd14f8c75ce917b485991e3
# unstake 0x97d5d0cdd02d28593e2d47de785eec4e1c6166383872761f263f970d14fe4e06
# stake 0xdbb5172f5f90a3280ce81f340109915497f23f713674715e41272adc08d0dff3


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


class MakeData():
    def get_logs_by_address(self, transaction_id, filename):
        '''Get transaction by address'''
        bsc_receipt = w3.eth.get_transaction_receipt(transaction_id)

        jsondata = Web3.toJSON(bsc_receipt)
        jsonfile = open("data/receipt/" + filename + ".json",
                        "w", encoding="utf-8")
        jsonfile.write(jsondata)
        jsonfile.close()

    def get_transaction(self, transaction_number, address):
        url = "https://api.bscscan.com/api?module=account&action=txlist&address=" + \
            address + "&startblock=0&endblock=99999999&page=1&offset=" + str(transaction_number) \
            + "&sort=" + ORDER + "&" + "apikey = " + \
            os.environ.get('BSC_SCAN_API')
        response = requests.get(url, verify=certifi.where())
        address_content = response.json()
        details = address_content.get("result")

        for index, transaction in enumerate(details):
            with open("data/header/" + FILENAME[index] + ".json", "w", encoding="utf-8") \
                    as outfile:
                json.dump(transaction, outfile)

            self.get_logs_by_address(transaction['hash'], FILENAME[index])


MakeData().get_transaction(TRANSACTION_NUMBER, ADDRESS)
