"""test """
import json
from src.header import Header


class TestHeader:

    def test_get_time_01(self):
        file = open("data/transaction/transaction1.json",
                    "r", encoding="utf-8")
        jsondata = json.load(file)
        file.close()
        time = Header(
            jsondata["timeStamp"], jsondata["gasPrice"], jsondata["gasUsed"]).get_time()
        assert time == "2021-12-28-01:28:52"

    def test_get_transaction_fee_01(self):
        file = open("data/transaction/transaction1.json",
                    "r", encoding="utf-8")
        jsondata = json.load(file)
        file.close()
        transaction_fee = Header(
            jsondata["timeStamp"], jsondata["gasPrice"], jsondata["gasUsed"]).get_transaction_fee()
        assert transaction_fee == "0.00067182"
