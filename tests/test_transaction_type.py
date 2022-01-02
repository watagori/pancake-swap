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


def test_get_transaction_to_01():
    file = open("data/receipt/transfer.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_transaction_to(
        jsondata) == "0xda28ecfc40181a6dad8b52723035dfba3386d26e"


def test_get_transaction_from_01():
    file = open("data/receipt/exchange_bnb_to_cake.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_transaction_from(
        jsondata) == "0xda28ecfc40181a6dad8b52723035dfba3386d26e"


def test_get_exchange_contract_address_from_01():
    file = open("data/receipt/exchange_bnb_to_cake.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_exchange_contract_address_from(
        jsondata) == "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c"


def test_get_exchange_contract_address_to_01():
    file = open("data/receipt/exchange_bnb_to_cake.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_exchange_contract_address_to(
        jsondata) == "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82"


def test_get_exchange_credit_amount_from_01():
    file = open("data/receipt/exchange_bnb_to_cake.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_exchange_credit_amount_from(
        jsondata) == "0.5"


def test_get_exchange_credit_amount_to_01():
    file = open("data/receipt/exchange_bnb_to_cake.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_exchange_credit_amount_to(
        jsondata) == "21.562948714728883817"


def test_get_liquidity_add_contract_address_debit_01():
    file = open("data/receipt/liquidity_bnb_and_cake_to_lp.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_liquidity_add_contract_address_debit(
        jsondata) == "0x0ed7e52944161450477ee417de9cd3a859b14fd0"


def test_get_liquidity_add_contract_address_credit_01():
    file = open("data/receipt/liquidity_bnb_and_cake_to_lp.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82" and \
        "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c" \
        in Logs().get_liquidity_add_contract_address_credit(
           jsondata)


def test_get_liquidity_add_amount_debit_01():
    file = open("data/receipt/liquidity_bnb_and_cake_to_lp.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_liquidity_add_amount_debit(
        jsondata) == "3.164332228458444898"


def test_get_liquidity_add_amount_credit_01():
    file = open("data/receipt/liquidity_bnb_and_cake_to_lp.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert "21.562948714728883817" and "0.497952988038470308" \
        in Logs().get_liquidity_add_amount_credit(jsondata)


def test_get_liquidity_remove_contract_address_debit():
    file = open("data/receipt/liquidity_lp_to_bnb_and_cake.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82" and \
        "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c" \
        in Logs().get_liquidity_remove_contract_address_debit(
            jsondata)


def test_get_liquidity_remove_contract_address_credit():
    file = open("data/receipt/liquidity_lp_to_bnb_and_cake.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_liquidity_remove_contract_address_credit(jsondata) == \
        "0x0ed7e52944161450477ee417de9cd3a859b14fd0"


def test_get_liquidity_remove_amount_debit_01():
    file = open("data/receipt/liquidity_lp_to_bnb_and_cake.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert "21.5721707333114908" and "0.497740943162833803" \
        in Logs().get_liquidity_remove_amount_debit(jsondata)


def test_get_liquidity_remove_amoubnt_credit_01():
    file = open("data/receipt/liquidity_lp_to_bnb_and_cake.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_liquidity_remove_amount_credit(
        jsondata) == "3.164332228458444898"


def test_get_transaction_fee_from_01():
    file = open("data/receipt/exchange_bnb_to_cake.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_transaction_fee_from(
        jsondata) == "0xda28ecfc40181a6dad8b52723035dfba3386d26e"


def test_get_transaction_fee_from_02():
    file = open("data/receipt/liquidity_bnb_and_cake_to_lp.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    assert Logs().get_transaction_fee_from(
        jsondata) == "0xda28ecfc40181a6dad8b52723035dfba3386d26e"


def test_get_transaction_fee_to_01():
    assert Logs().get_transaction_fee_to(
    ) == "0x0000000000000000000000000000000000000000"


def test_get_transaction_exchange_detail():
    file = open("data/receipt/exchange_bnb_to_cake.json",
                "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    file_transaction = open(
        "data/transaction/transaction1.json", "r", encoding="utf-8")
    jsondata_transaction = json.load(file_transaction)
    file_transaction.close()
    assert Logs().get_transaction_exchange_detail(
        jsondata, jsondata_transaction) == {
        "time": "2021-12-28-01:28:52",
        "platform": "bnb_pancakeswap",
        "transaction_hash":
            "0x4f8534e85849cb54f0ae4ca0718939ab22de248f64e2e4dc607a76b12f20f109",
        "debit_title": "SPOT",
        "debit_amount": {"CAKE": "21.562948714728883817"},
        "debit_from": "0x10ed43c718714eb63d5aa57b78b54704e256024e",
        "debit_to": "0xda28ecfc40181a6dad8b52723035dfba3386d26e",
        "credit_title": "SPOT",
        "credit_amount": {"BNB": "0.5"},
        "credit_from": "0xda28ecfc40181a6dad8b52723035dfba3386d26e",
        "credit_to": "0x10ed43c718714eb63d5aa57b78b54704e256024e",
    }
