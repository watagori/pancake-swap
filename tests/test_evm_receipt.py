"""test evm logs file"""
import json
from src.evm_receipt import EvmReceipt


class TestEvmReceipt:
    def test_get_type_01(self):
        file = open("data/receipt/approve.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        transaction_type = EvmReceipt(
            receipt["logs"], receipt["from"], receipt["to"])\
            .get_transaction_type()
        assert transaction_type == "approve"

    def test_get_type_02(self):
        file = open("data/receipt/transfer.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        transaction_type = EvmReceipt(
            receipt["logs"], receipt["from"], receipt["to"])\
            .get_transaction_type()
        assert transaction_type == "transfer"

    def test_get_type_03(self):
        file = open("data/receipt/exchange_bnb_to_cake.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        transaction_type = EvmReceipt(
            receipt["logs"], receipt["from"], receipt["to"])\
            .get_transaction_type()
        assert transaction_type == "exchange"

    def test_get_type_04(self):
        file = open("data/receipt/exchange_cake_to_bnb.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        transaction_type = EvmReceipt(
            receipt["logs"], receipt["from"], receipt["to"])\
            .get_transaction_type()
        assert transaction_type == "exchange"

    def test_get_type_05(self):
        file = open("data/receipt/liquidity_bnb_and_cake_to_lp.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        transaction_type = EvmReceipt(
            receipt["logs"], receipt["from"], receipt["to"])\
            .get_transaction_type()
        assert transaction_type == "add-liquidity"

    def test_get_type_06(self):
        file = open("data/receipt/liquidity_lp_to_bnb_and_cake.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        transaction_type = EvmReceipt(
            receipt["logs"], receipt["from"], receipt["to"])\
            .get_transaction_type()
        assert transaction_type == "remove-liquidity"

    def test_get_from_address_01(self):
        file = open("data/receipt/approve.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        from_address = EvmReceipt(
            receipt["logs"], receipt["from"], receipt["to"])\
            .get_from_address()
        assert from_address == "0xda28ecfc40181a6dad8b52723035dfba3386d26e"

    def test_get_to_address_01(self):
        file = open("data/receipt/approve.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        to_address = EvmReceipt(
            receipt["logs"], receipt["from"], receipt["to"])\
            .get_to_address()
        assert to_address == "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82"

    def test_get_exchange_credit_token_01(self):
        file = open("data/receipt/exchange_bnb_to_cake.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        from_token_address = EvmReceipt(
            receipt["logs"], receipt["from"], receipt["to"])\
            .get_exchange_credit_token()
        assert from_token_address == "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c"

    def test_get_exchange_debit_token01(self):
        file = open("data/receipt/exchange_bnb_to_cake.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        to_token_address = EvmReceipt(
            receipt["logs"], receipt["from"], receipt["to"])\
            .get_exchange_debit_token()
        assert to_token_address == "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82"

    def test_get_exchange_credit_amount_01(self):
        file = open("data/receipt/exchange_bnb_to_cake.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        from_amount = EvmReceipt(
            receipt["logs"], receipt["from"], receipt["to"])\
            .get_exchange_credit_amount()
        assert from_amount == "0.5"

    def test_get_exchange_debit_amount_01(self):
        file = open("data/receipt/exchange_bnb_to_cake.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        to_amount = EvmReceipt(
            receipt["logs"], receipt["from"], receipt["to"])\
            .get_exchange_debit_amount()
        assert to_amount == "21.562948714728883817"

    def test_get_liquidity_add_credit_token_01(self):
        file = open("data/receipt/liquidity_bnb_and_cake_to_lp.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        from_token_address = EvmReceipt(
            receipt["logs"], receipt["from"], receipt["to"])\
            .get_liquidity_add_credit_token()
        assert "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82" and \
            "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c" in from_token_address

    def test_get_liquidity_add_debit_token_01(self):
        file = open("data/receipt/liquidity_bnb_and_cake_to_lp.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        to_token_address = EvmReceipt(
            receipt["logs"], receipt["from"], receipt["to"])\
            .get_liquidity_add_debit_token()
        assert to_token_address == "0x0ed7e52944161450477ee417de9cd3a859b14fd0"

    def test_get_liquidity_add_credit_amount_01(self):
        file = open("data/receipt/liquidity_bnb_and_cake_to_lp.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        from_amount = EvmReceipt(
            receipt["logs"], receipt["from"], receipt["to"])\
            .get_liquidity_add_credit_amount()
        assert "0.497952988038470308" and \
            "21.562948714728883817" in from_amount

    def test_get_liquidity_add_debit_amount_01(self):
        file = open("data/receipt/liquidity_bnb_and_cake_to_lp.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        to_amount = EvmReceipt(
            receipt["logs"], receipt["from"], receipt["to"])\
            .get_liquidity_add_debit_amount()
        assert to_amount == "3.164332228458444898"

    def test_get_liquidity_remove_credit_token_01(self):
        file = open("data/receipt/liquidity_lp_to_bnb_and_cake.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        credit_token = EvmReceipt(
            receipt["logs"], receipt["from"], receipt["to"])\
            .get_liquidity_remove_credit_token()
        assert credit_token == "0x0ed7e52944161450477ee417de9cd3a859b14fd0"

    def test_get_liquidity_remove_debit_token_01(self):
        file = open("data/receipt/liquidity_lp_to_bnb_and_cake.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        debit_token = EvmReceipt(
            receipt["logs"], receipt["from"], receipt["to"])\
            .get_liquidity_remove_debit_token()
        assert "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82" and \
            "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c" in debit_token

    def test_get_liquidity_remove_credit_amount_01(self):
        file = open("data/receipt/liquidity_lp_to_bnb_and_cake.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        credit_amount = EvmReceipt(
            receipt["logs"], receipt["from"], receipt["to"])\
            .get_liquidity_remove_credit_amount()
        assert credit_amount == "3.164332228458444898"

    def test_get_liquidity_remove_debit_amount_01(self):
        file = open("data/receipt/liquidity_lp_to_bnb_and_cake.json",
                    "r", encoding="utf-8")
        receipt = json.load(file)
        file.close()
        debit_amount = EvmReceipt(
            receipt["logs"], receipt["from"], receipt["to"])\
            .get_liquidity_remove_debit_amount()
        assert "21.5721707333114908" and "0.497740943162833803" \
            in debit_amount
