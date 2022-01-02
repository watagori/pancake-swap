# receipt by w3.eth.get_transaction_receipt(transaction_hash)
import json
from src.transaction_type import Logs


def test_swap_type_01():
    file = open("data/receipt/exchange_bnb_to_cake.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_swap_type(jsondata) is True


def test_get_transaction_type_01():

    file = open("data/receipt/approve_cake_max.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_transaction_type(jsondata) == "approve"


def test_get_transaction_type_02():
    file = open("data/receipt/exchange_bnb_to_cake.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_transaction_type(jsondata) == "exchange"


def test_get_transaction_type_03():
    file = open("data/receipt/exchange_cake_to_bnb.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_transaction_type(jsondata) == "exchange"


def test_get_transaction_type_04():
    file = open("data/receipt/liquidity_bnb_and_cake_to_lp.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_transaction_type(jsondata) == "add-liquidity"


def test_get_transaction_type_05():
    file = open("data/receipt/liquidity_lp_to_bnb_and_cake.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_transaction_type(jsondata) == "remove-liquidity"


def test_get_transaction_type_06():
    file = open("data/receipt/transfer.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_transaction_type(jsondata) == "transfer"


def test_transaction_to_01():
    file = open("data/receipt/transfer.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_transaction_to(
        jsondata) == "0xda28ecfc40181a6dad8b52723035dfba3386d26e"


def test_transaction_to_02():
    file = open("data/receipt/exchange_bnb_to_cake.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_transaction_to(
        jsondata) == "0x10ed43c718714eb63d5aa57b78b54704e256024e"


def test_exchange_contract_address_from_01():
    file = open("data/receipt/exchange_bnb_to_cake.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_exchange_contract_address_from(
        jsondata) == "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c"


def test_exchange_contract_address_to_01():
    file = open("data/receipt/exchange_bnb_to_cake.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_exchange_contract_address_to(
        jsondata) == "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82"
