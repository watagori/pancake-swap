"""test """
import json
from src.header import Header


class TestHeader:

    def test_get_time_01(self):
        file = open("data/header/exchange_bnb_to_cake.json",
                    "r", encoding="utf-8")
        header = json.load(file)
        file.close()
        time = Header(
            header).get_time()
        assert time == "2021-12-28-01:28:52"

    def test_get_fee_amount_01(self):
        file = open("data/header/exchange_bnb_to_cake.json",
                    "r", encoding="utf-8")
        header = json.load(file)
        file.close()
        transaction_fee = Header(
            header)\
            .get_transaction_fee()
        assert transaction_fee == "0.00067182"

    def test_get_fee_from_01(self):
        file = open("data/header/exchange_bnb_to_cake.json",
                    "r", encoding="utf-8")
        header = json.load(file)
        file.close()
        fee_from = Header(
            header)\
            .get_transaction_from()
        assert fee_from == "0xda28ecfc40181a6dad8b52723035dfba3386d26e"

    def test_get_transaction_hash_01(self):
        file = open("data/header/exchange_bnb_to_cake.json",
                    "r", encoding="utf-8")
        header = json.load(file)
        file.close()
        transaction_hash = Header(header).get_transaction_hash()
        assert transaction_hash ==\
            "0x4f8534e85849cb54f0ae4ca0718939ab22de248f64e2e4dc607a76b12f20f109"

    def test_get_transaction_to_01(self):
        file = open("data/header/approve.json",
                    "r", encoding="utf-8")
        header = json.load(file)
        file.close()
        transaction_to = Header(header).get_transaction_to()
        assert transaction_to == "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82"

    def test_get_transaction_to_02(self):
        file = open("data/header/exchange_bnb_to_cake.json",
                    "r", encoding="utf-8")
        header = json.load(file)
        file.close()
        transaction_to = Header(header).get_transaction_to()
        assert transaction_to == "0x10ed43c718714eb63d5aa57b78b54704e256024e"
