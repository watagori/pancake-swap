# receipt by w3.eth.get_transaction_receipt(transaction_hash)
import json
from src.transaction_receipt import Logs


class TestTransactionType:
    def test_approve_01(self):

        file = open("data/receipt/approve_cake_max.json",
                    "r", encoding="utf-8")
        jsondata = json.load(file)
        file.close()
        assert Logs().get_transaction_type(jsondata) == "approve"

    def test_deposit_01(self):
        file = open("data/receipt/exchange_bnb_to_cake.json",
                    "r", encoding="utf-8")
        jsondata = json.load(file)
        file.close()
        assert Logs().get_transaction_type(jsondata) == "exchange-bnb"

    def test_exchange_cake_to_bnb_01(self):
        file = open("data/receipt/exchange_cake_to_bnb.json",
                    "r", encoding="utf-8")
        jsondata = json.load(file)
        file.close()
        assert Logs().get_transaction_type(jsondata) == "exchange"

    def test_liquidity_bnb_and_cake_to_lp_01(self):
        file = open("data/receipt/liquidity_bnb_and_cake_to_lp.json",
                    "r", encoding="utf-8")
        jsondata = json.load(file)
        file.close()
        assert Logs().get_transaction_type(jsondata) == "add-liquidity"

    def test_liquidity_lp_to_bnb_and_cake_01(self):
        file = open("data/receipt/liquidity_lp_to_bnb_and_cake.json",
                    "r", encoding="utf-8")
        jsondata = json.load(file)
        file.close()
        assert Logs().get_transaction_type(jsondata) == "remove-liquidity"


def test_to():
    assert Logs().get_to() == "0x0000000000000000000000000000000000000000"
