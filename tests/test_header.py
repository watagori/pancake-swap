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
            .get_fee_from()
        assert fee_from == "0xda28ecfc40181a6dad8b52723035dfba3386d26e"

    def test_get_fee_to_01(self):
        file = open("data/header/exchange_bnb_to_cake.json",
                    "r", encoding="utf-8")
        header = json.load(file)
        file.close()
        fee_to = Header(
            header)\
            .get_fee_to()
        assert fee_to == "0x0000000000000000000000000000000000000000"
