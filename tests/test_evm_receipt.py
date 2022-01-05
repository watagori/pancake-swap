"""test evm logs file"""
import json
from src.evm_receipt import EvmReceipt
import re


class TestEvmReceipt:
    def test_get_result_00(self):
        file = open("data/receipt/transfer.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        result = EvmReceipt(receipt).get_result()
        result_target = {'type': 'transfer'}

        assert result == result_target

    def test_get_result_01(self):
        file = open("data/receipt/approve.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        result = EvmReceipt(receipt).get_result()
        result_target = {
            "type": "approve",
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
            "type": "exchange",
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
            "type": "exchange",
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
        result["from_token_amount"].sort(key=self.natural_keys)
        result["from_token_address"].sort(key=self.natural_keys)
        result_target = {
            "type": "add_liquidity",
            "from_address": "0xda28ecfc40181a6dad8b52723035dfba3386d26e",
            "to_address": "0x10ed43c718714eb63d5aa57b78b54704e256024e",
            "from_token_address": ["0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82",
                                   "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c"],
            "to_token_address": "0x0ed7e52944161450477ee417de9cd3a859b14fd0",
            "from_token_amount": ["0.497952988038470308", "21.562948714728883817"],
            "to_token_amount": "3.164332228458444898",
        }

        assert result == result_target

    def test_get_result_05(self):
        file = open("data/receipt/liquidity_lp_to_bnb_and_cake.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        result = EvmReceipt(receipt).get_result()
        result["to_token_amount"].sort(key=self.natural_keys)
        result["to_token_address"].sort(key=self.natural_keys)
        result_target = {
            "type": "remove_liquidity",
            "from_address": "0xda28ecfc40181a6dad8b52723035dfba3386d26e",
            "to_address": "0x10ed43c718714eb63d5aa57b78b54704e256024e",
            "to_token_address": ["0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82",
                                 "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c"],
            "from_token_address": "0x0ed7e52944161450477ee417de9cd3a859b14fd0",
            "to_token_amount": ["0.497740943162833803", "21.5721707333114908"],
            "from_token_amount": "3.164332228458444898"
        }

        assert result == result_target

    def atof(self, text):
        try:
            retval = float(text)
        except ValueError:
            retval = text
        return retval

    def natural_keys(self, text):
        '''
        alist.sort(key=natural_keys) sorts in human order
        http://nedbatchelder.com/blog/200712/human_sorting.html
        (See Toothy's implementation in the comments)
        float regex comes from https://stackoverflow.com/a/12643073/190597
        '''
        return [self.atof(c) for c in re.split(r'[+-]?([0-9]+(?:[.][0-9]*)?|[.][0-9]+)', text)]
