import json
from src.logs import Logs


def test_approve_01():
    file = open("data/logs/approve_cake_max.json", "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_transaction_type(jsondata) == "approve"


def test_deposit_01():
    file = open("data/logs/exchange_bnb_to_cake.json", "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_transaction_type(jsondata) == "exchange-bnb"


def test_exchange_cake_to_bnb_01():
    file = open("data/logs/exchange_cake_to_bnb.json", "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_transaction_type(jsondata) == "exchange"


def test_liquidity_bnb_and_cake_to_lp_01():
    file = open("data/logs/liquidity_bnb_and_cake_to_lp.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_transaction_type(jsondata) == "add-liquidity"


def test_liquidity_lp_to_bnb_and_cake_01():
    file = open("data/logs/liquidity_lp_to_bnb_and_cake.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_transaction_type(jsondata) == "remove-liquidity"
