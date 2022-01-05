import json
import csv
from src.caaj_converter import CaajConverter


class TestCaajConverter:
    def test_caaj_converter_01(self):

        file_name = "exchange_bnb_to_cake.json"
        header_file = open("data/header/" + file_name,
                           "r", encoding="utf-8")
        header_data = json.load(header_file)
        header_file.close()
        receipt_file = open("data/receipt/" + file_name,
                            "r", encoding="utf-8")
        receipt_data = json.load(receipt_file)
        receipt_file.close()
        caaj_data = CaajConverter(header_data, receipt_data).get_caaj()
        caaj_data_model = [{
            "time": "2021-12-28-01:28:52",
            "platfrom": "bnb_pancakeswap",
            "transaction_id": "0x4f8534e85849cb54f0ae4ca0718939ab22de248f64e2e4dc607a76b12f20f109",
            "debit_title": "SPOT",
            "debit_amount": {"CAKE": "21.562948714728883817"},
            "debit_from": "0x10ed43c718714eb63d5aa57b78b54704e256024e",
            "debit_to": "0xda28ecfc40181a6dad8b52723035dfba3386d26e",
            "credit_title": "SPOT",
            "credit_amount": {"BNB": "0.5"},
            "credit_from": "0xda28ecfc40181a6dad8b52723035dfba3386d26e",
            "credit_to": "0x10ed43c718714eb63d5aa57b78b54704e256024e",
            "comment": "pancakeswap trade"
        },
            {
            "time": "2021-12-28-01:28:52",
            "platfrom": "bnb_pancakeswap",
            "transaction_id": "0x4f8534e85849cb54f0ae4ca0718939ab22de248f64e2e4dc607a76b12f20f109",
            "debit_title": "SPOT",
            "debit_amount": {"BNB": "0.00067182"},
            "debit_from": "0x0000000000000000000000000000000000000000",
            "debit_to": "0xda28ecfc40181a6dad8b52723035dfba3386d26e",
            "credit_title": "SPOT",
            "credit_amount":  {"BNB": "0.00067182"},
            "credit_from": "0xda28ecfc40181a6dad8b52723035dfba3386d26e",
            "credit_to": "0x0000000000000000000000000000000000000000",
            "comment": "pancakeswap fee"
        }]

        assert caaj_data == caaj_data_model

    def test_caaj_converter_02(self):

        file_name = "liquidity_bnb_and_cake_to_lp.json"
        header_file = open("data/header/" + file_name,
                           "r", encoding="utf-8")
        header_data = json.load(header_file)
        header_file.close()
        receipt_file = open("data/receipt/" + file_name,
                            "r", encoding="utf-8")
        receipt_data = json.load(receipt_file)
        receipt_file.close()
        caaj_data = CaajConverter(header_data, receipt_data).get_caaj()
        caaj_data_model = [{
            "time": "2021-12-28-01:31:49",
            "platfrom": "bnb_pancakeswap",
            "transaction_id": "0xb4c3ed5db127089cd1be4b247537d163e74e99e33598348579ffae4f81877834",
            "debit_title": "LIQUIDITY",
            "debit_amount": {"0x0ed7e52944161450477ee417de9cd3a859b14fd0": "3.164332228458444898"},
            "debit_from": "0x10ed43c718714eb63d5aa57b78b54704e256024e",
            "debit_to": "0xda28ecfc40181a6dad8b52723035dfba3386d26e",
            "credit_title": "SPOT",
            "credit_amount": {"BNB": "0.497952988038470308", "CAKE": "21.562948714728883817"},
            "credit_from": "0xda28ecfc40181a6dad8b52723035dfba3386d26e",
            "credit_to": "0x10ed43c718714eb63d5aa57b78b54704e256024e",
            "comment": "pancakeswap add liquidity"
        },
            {
            "time": "2021-12-28-01:31:49",
            "platfrom": "bnb_pancakeswap",
            "transaction_id": "0xb4c3ed5db127089cd1be4b247537d163e74e99e33598348579ffae4f81877834",
            "debit_title": "SPOT",
            "debit_amount": {"BNB": "0.00094686"},
            "debit_from": "0x0000000000000000000000000000000000000000",
            "debit_to": "0xda28ecfc40181a6dad8b52723035dfba3386d26e",
            "credit_title": "SPOT",
            "credit_amount":  {"BNB": "0.00094686"},
            "credit_from": "0xda28ecfc40181a6dad8b52723035dfba3386d26e",
            "credit_to": "0x0000000000000000000000000000000000000000",
            "comment": "pancakeswap fee"
        }]
        assert caaj_data == caaj_data_model
