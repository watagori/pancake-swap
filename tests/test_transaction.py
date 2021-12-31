import json
from src.transaction import Transaction


def test_hash():
    file = open("data/transaction/transaction0.json", "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    transactoin_hash = Transaction().get_hash(jsondata)
    assert transactoin_hash == "0x79735e1af5d4fbc1d68172e10fcf44c6af00916f35727f8838fac5e71b5c48f6"


def test_time():
    file = open("data/transaction/transaction0.json", "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    transactoin_time = Transaction().get_time(jsondata)
    assert transactoin_time == "2021-12-31-03:02:43"


def test_transaction_fee():
    file = open("data/transaction/transaction0.json", "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    transactoin_fee = Transaction().get_transaction_fee(jsondata)
    assert transactoin_fee == "0.000641925"
