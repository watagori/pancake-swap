import json
from src.logs import Logs


def test_approve_01():
    file = open("data/approve_cake_max.json", "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_transaction_type(jsondata) == "approve"


def test_exchange_bnb_to_cake_01():
    file = open("data/exchange_bnb_to_cake.json", "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_transaction_type(jsondata) == "exchange"


def test_exchange_cake_to_bnb_01():
    file = open("data/exchange_cake_to_bnb.json", "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_transaction_type(jsondata) == "exchange"


def test_liquidity_bnb_and_cake_to_lp_01():
    file = open("data/liquidity_bnb_and_cake_to_lp.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_transaction_type(jsondata) == "liquidity"
