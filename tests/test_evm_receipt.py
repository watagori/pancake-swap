"""test evm logs file"""
import json
from src.evm_receipt import EvmReceipt


class TestEvmReceipt:
    def test_get_result_00(self):
        file = open("data/receipt/transfer.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        result = EvmReceipt(receipt).get_result()
        result_target = "transfer"

        assert result == result_target

    def test_get_result_01(self):
        file = open("data/receipt/approve.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        result = EvmReceipt(receipt).get_result()
        result_target = {
            "platform": "bnb_pancakeswap",
            "transaction_type": "approve",
            "from_address": "0xda28ecfc40181a6dad8b52723035dfba3386d26e",
            "to_address": "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82",
        }

        assert result == result_target

    def test_get_result_02(self):
        file = open("data/receipt/exchange_bnb_to_cake.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        result = EvmReceipt(receipt).get_result()
        result_target = {
            "platform": "bnb_pancakeswap",
            "transaction_type": "exchange",
            "from_address": "0xda28ecfc40181a6dad8b52723035dfba3386d26e",
            "to_address": "0x10ed43c718714eb63d5aa57b78b54704e256024e",
            "from_token_address": "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c",
            "to_token_address": "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82",
            "from_token_amount": "0.5",
            "to_token_amount": "21.562948714728883817",
        }

        assert result == result_target

    def test_get_result_03(self):
        file = open("data/receipt/exchange_cake_to_bnb.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        result = EvmReceipt(receipt).get_result()
        result_target = {
            "platform": "bnb_pancakeswap",
            "transaction_type": "exchange",
            "from_address": "0xda28ecfc40181a6dad8b52723035dfba3386d26e",
            "to_address": "0x10ed43c718714eb63d5aa57b78b54704e256024e",
            "to_token_address": "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c",
            "from_token_address": "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82",
            "to_token_amount": "0.496512815787098187",
            "from_token_amount": "21.5721707333114908",
        }

        assert result == result_target

    def test_get_result_04(self):
        file = open("data/receipt/liquidity_bnb_and_cake_to_lp.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        result = EvmReceipt(receipt).get_result()
        result_target = {
            "platform": "bnb_pancakeswap",
            "transaction_type": "add-liquidity",
            "from_address": "0xda28ecfc40181a6dad8b52723035dfba3386d26e",
            "to_address": "0x10ed43c718714eb63d5aa57b78b54704e256024e",
            "from_token_address": {"0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c",
                                   "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82"},
            "to_token_address": "0x0ed7e52944161450477ee417de9cd3a859b14fd0",
            "from_token_amount": {"21.562948714728883817", "0.497952988038470308"},
            "to_token_amount": "3.164332228458444898",
        }

        assert result == result_target

    def test_get_result_05(self):
        file = open("data/receipt/liquidity_lp_to_bnb_and_cake.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        result = EvmReceipt(receipt).get_result()
        result_target = {
            "platform": "bnb_pancakeswap",
            "transaction_type": "remove-liquidity",
            "from_address": "0xda28ecfc40181a6dad8b52723035dfba3386d26e",
            "to_address": "0x10ed43c718714eb63d5aa57b78b54704e256024e",
            "to_token_address": {"0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c",
                                 "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82"},
            "from_token_address": "0x0ed7e52944161450477ee417de9cd3a859b14fd0",
            "to_token_amount": {"21.5721707333114908", "0.497740943162833803"},
            "from_token_amount": "3.164332228458444898"
        }

        assert result == result_target
