import json
from src.transaction import Transaction


def test_hash():
    file = open("data/transaction/transaction1.json", "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    transactoin_hash = Transaction().get_hash(jsondata)
    assert transactoin_hash == "0x4f8534e85849cb54f0ae4ca0718939ab22de248f64e2e4dc607a76b12f20f109"


def test_time():
    file = open("data/transaction/transaction1.json", "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    transactoin_time = Transaction().get_time(jsondata)
    assert transactoin_time == "2021-12-28-01:28:52"


def test_transaction_fee():
    file = open("data/transaction/transaction1.json", "r", encoding="utf-8")
    jsondata = json.load(file)
    file.close()
    transactoin_fee = Transaction().get_transaction_fee(jsondata)
    assert transactoin_fee == "0.00067182"
