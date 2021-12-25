"""Get the details of the transaction obtained by get_transaction_list.py"""
import csv
from decimal import Decimal
from datetime import datetime
from web3 import Web3


ERC20_APPROVE_TOPIC = '0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925'


BSC_URL = "https://bsc-dataseed.binance.org/"

w3 = Web3(Web3.HTTPProvider(BSC_URL))

gwei = Decimal(1000000000000000000)


def get_transaction_detail(transaction, transaction_number, address, platform_name):
    '''Get the details of the transaction and output .csv.

    Args:
        transaction: transaction
        transaction_number: index of the transaction lists
        address: address of the transaction
        platform_name: name of the platform(ex. PancakeSwap)
    '''
    transaction_id = transaction.get("hash")

    time_stamp = transaction.get("timeStamp")
    date_object = datetime.fromtimestamp(int(time_stamp))
    # eth_value = Decimal(value)/gwei
    f_detail = open("dist/transactions_detail.csv", "a", encoding='UTF-8')
    writer_detail = csv.writer(f_detail)

    bsc_receipt = w3.eth.get_transaction_receipt(transaction_id)
    logs = bsc_receipt['logs']

    writer_detail.writerow(
        [date_object, "PancakeSwap", transaction_id, bsc_receipt['from'], bsc_receipt['to']])
    f_detail.close()

    # common caaj'values
    time = time_stamp
    platform = platform_name

    debit_amount_fee = Decimal(
        bsc_receipt['gasUsed'])*Decimal(transaction['gasPrice'])/gwei
    credit_amount = Decimal(transaction.get("value"))/gwei

    f_caaj = open("dist/caaj_pancake.csv", "a", encoding='UTF-8')
    writer_caaj = csv.writer(f_caaj)
    print(transaction_number)
    # if logs[0]["topics"][0].hex().lower() == ERC20_APPROVE_TOPIC:
    debit_amount_fee = Decimal(
        bsc_receipt['gasUsed'])*Decimal(transaction['gasPrice'])/gwei
    print(debit_amount_fee)
    devit__title = "FEE"
    debit_amount = debit_amount_fee
    debit_from = "0x0000000000000000000000000000000000000000"
    debit_to = address
    credit_title = "SPOT"
    credit_amount = debit_amount_fee
    credit_from = address
    credit_to = "0x0000000000000000000000000000000000000000"
    writer_caaj.writerow([time, platform, transaction_id, devit__title, debit_amount,
                          debit_from, debit_to, credit_title, credit_amount,
                          credit_from, credit_to])

    # print(input_transfers)
    # for i in len(logs):
    #     print(logs[i]["topics"])
    print("\n")
