"""Get the details of the transaction obtained by get_transaction_list.py"""
import os
import csv
from decimal import Decimal
from datetime import datetime
from web3 import Web3

# transaction history
# transafer(waki -> nishi) 0x57932a25175a1184d433be880655d1ee6d1a9e62853723e695f1d38553914462
# exchange(BNB -> CAKE) 0x4f8534e85849cb54f0ae4ca0718939ab22de248f64e2e4dc607a76b12f20f109
# CAKE max approve 0x36512c7e09e3570dfc53176252678ee9617660550d36f4da797afba6fc55bba6
# liquidity(BNB + CAKE -> LP) 0xb4c3ed5db127089cd1be4b247537d163e74e99e33598348579ffae4f81877834
# liquidity(LP -> BNB + CAKE) 0xdc70901bcb2517a885e41ab9ccb0a739ae73af4b8862a1c46f9ca2ce583b8cd3
# exchange(CAKE -> BNB) 0xd3f63cdad3bb1b8ea46fafbaac21c93cdb7204daece60f1a44aaa198f58371fa

WETH_CONTRACT_ADDRESS = '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'
WETH_DEPOSIT_TOPIC = '0xe1fffcc4923d04b559f4d29a8bfc6cda04eb5b0d3c460751c2402c5c5cc9109c'
WETH_WITHDRAWAL_TOPIC = '0x7fcf532c15f0a6db0bd6d0e038bea71d30d808c7d98cb3bf7268a95bf5081b65'

ERC20_TRANSFER_TOPIC = '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
ERC20_APPROVE_TOPIC = '0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925'

PANCAKE_CONTRACT_ADDRESS = '0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82'
WBNB_CONTRACT_ADDRESS = '0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c'

PANCAKE_ROUTER_V2_ADDRESS = "0x10ed43c718714eb63d5aa57b78b54704e256024e"

BSC_URL = "https://bsc-dataseed.binance.org/"

w3 = Web3(Web3.HTTPProvider(BSC_URL))
gwei = Decimal(1000000000000000000)


def get_transaction_detail(transaction, transaction_number, my_address, platform_name):
    '''Get the details of the transaction and output .csv.

    Args:
        transaction: transaction
        transaction_number: index of the transaction lists
        address: account address of the transaction
        platform_name: name of the platform(ex. PancakeSwap)
    '''
    transaction_id = transaction.get("hash")
    time_stamp = transaction.get("timeStamp")
    date_object = datetime.fromtimestamp(int(time_stamp))
    # eth_value = Decimal(value)/gwei

    bsc_receipt = w3.eth.get_transaction_receipt(transaction_id)
    logs = bsc_receipt['logs']

    # common caaj'values
    time = date_object.strftime("%Y-%m-%d %H:%M:%S")
    platform = platform_name
    # transaction_id = transaction_id
    debit_amount_fee = Decimal(
        bsc_receipt['gasUsed'])*Decimal(transaction['gasPrice'])/gwei
    # credit_amount = Decimal(transaction.get("value"))/gwei

# caaj csv file
    file_dir = "dist/caaj_lancake.csv"
    if os.path.exists(file_dir) and transaction_number == 0:
        os.remove(file_dir)

    f_caaj = open(file_dir, "a", encoding='UTF-8')
    writer_caaj = csv.writer(f_caaj)

    if len(logs) == 0:
        # transfer(waki -> nishi)
        # transfer info
        # time = date_object.strftime("%Y-%m-%d %H:%M:%S")
        # platform = platform_name
        # transaction_id = transaction_id
        debit_title = "SPOT"
        debit_amount = str(Decimal(transaction.get("value"))/gwei)
        debit_from = bsc_receipt['to'].lower()
        debit_to = bsc_receipt['from'].lower()
        credit_title = "SPOT"
        credit_amount = str(Decimal(transaction.get("value"))/gwei)
        credit_from = bsc_receipt['from'].lower()
        credit_to = bsc_receipt['to'].lower()
        comment = "transfer"
        writer_caaj.writerow([time, platform, transaction_id, debit_title, debit_amount,
                              debit_from, debit_to, credit_title, credit_amount,
                              credit_from, credit_to, comment])

        # fee
        debit_title = "FEE"
        debit_amount = {"BNB": str(debit_amount_fee)}
        debit_from = "0x0000000000000000000000000000000000000000"
        debit_to = bsc_receipt['from'].lower()
        credit_title = "SPOT"
        credit_amount = {"BNB": str(debit_amount_fee)}
        credit_from = bsc_receipt['from'].lower()
        credit_to = "0x0000000000000000000000000000000000000000"
        comment = "transfer Fee"
        writer_caaj.writerow([time, platform, transaction_id, debit_title, debit_amount,
                              debit_from, debit_to, credit_title, credit_amount,
                              credit_from, credit_to, comment])

    elif len(logs) == 1 and logs[0]['topics'][0].hex().lower() == ERC20_APPROVE_TOPIC:
        # Approve fee
        debit_title = "FEE"
        debit_amount = {"BNB": str(debit_amount_fee)}
        debit_from = "0x0000000000000000000000000000000000000000"
        debit_to = bsc_receipt['from'].lower()
        credit_title = "SPOT"
        credit_amount = {"BNB": str(debit_amount_fee)}
        credit_from = bsc_receipt['from'].lower()
        credit_to = "0x0000000000000000000000000000000000000000"
        comment = "CAKE max Approve"
        writer_caaj.writerow([time, platform, transaction_id, debit_title, debit_amount,
                              debit_from, debit_to, credit_title, credit_amount,
                              credit_from, credit_to, comment])

    elif logs[0]['topics'][0].hex().lower() == WETH_DEPOSIT_TOPIC:
        # exchange(BNB -> CAKE)
        debit_amout_exchange = int(logs[0]['data'], 16)/gwei
        credit_amount_exchange = int(logs[2]['data'], 16)/gwei
        debit_title = "SPOT"
        debit_amount = {"CAKE": str(credit_amount_exchange)}
        debit_from = PANCAKE_ROUTER_V2_ADDRESS
        debit_to = my_address
        credit_title = "SPOT"
        credit_amount = {"BNB": str(debit_amout_exchange)}
        credit_from = my_address
        credit_to = PANCAKE_ROUTER_V2_ADDRESS
        comment = "exchange(BNB -> CAKE)"
        writer_caaj.writerow([time, platform, transaction_id, debit_title, debit_amount,
                              debit_from, debit_to, credit_title, credit_amount,
                              credit_from, credit_to, comment])

        debit_title = "FEE"
        debit_amount = {"BNB": str(debit_amount_fee)}
        debit_from = "0x0000000000000000000000000000000000000000"
        debit_to = bsc_receipt['from'].lower()
        credit_title = "SPOT"
        credit_amount = {"BNB": str(debit_amount_fee)}
        credit_from = bsc_receipt['from'].lower()
        credit_to = "0x0000000000000000000000000000000000000000"
        comment = "Exchange Fee"
        writer_caaj.writerow([time, platform, transaction_id, debit_title, debit_amount,
                              debit_from, debit_to, credit_title, credit_amount,
                              credit_from, credit_to, comment])

    f_caaj.close()
# make caaj file

    # if logs[0]["topics"][0].hex().lower() == ERC20_APPROVE_TOPIC:
    # debit_amount_fee = Decimal(
    #     bsc_receipt['gasUsed'])*Decimal(transaction['gasPrice'])/gwei
    # debit_title = "FEE"
    # debit_amount = debit_amount_fee
    # debit_from = "0x0000000000000000000000000000000000000000"
    # debit_to = address
    # credit_title = "SPOT"
    # credit_amount = debit_amount_fee
    # credit_from = address
    # credit_to = "0x0000000000000000000000000000000000000000"
    # writer_caaj.writerow([time, platform, transaction_id, debit_title, debit_amount,
    #                       debit_from, debit_to, credit_title, credit_amount,
    #                       credit_from, credit_to])
