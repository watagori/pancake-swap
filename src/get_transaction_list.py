'''Get list of the transaciton by any address'''
import csv
from decimal import Decimal
from datetime import datetime
import certifi
import requests
import get_transaction_detail


def get_transaction_by_address(address, transaction_number, platform_name):
    '''Get the list of the transaction by any address.
    Args:
        address: address of the transaction
        transaction_number: number of the transaction
        platform_name: name of the platform(ex. PancakeSwap)
    '''

    f_list = open("dist/transaction_list.csv", "w", encoding='UTF-8')
    writer = csv.writer(f_list)
    writer.writerow(["status", "transaction_id", "tx_from",
                    "tx_to", "value", "eth_value", "time_stamp", "datetime"])
    url = "https://api.bscscan.com/api?module=account&action=txlist&address=" + address \
        + "&startblock=0&endblock=99999999&page=1&offset=" + str(transaction_number) \
        + "&sort=desc&apikey=TBY4C25PY394RSWTF6DUXWCHJTYF8Q8H1U"
    response = requests.get(url, verify=certifi.where())
    address_content = response.json()
    details = address_content.get("result")

    for index, transaction in enumerate(details):
        transaction_id = transaction.get("hash")
        tx_from = transaction.get("from")
        tx_to = transaction.get("to")
        value = transaction.get("value")
        time_stamp = transaction.get("timeStamp")
        date_object = datetime.fromtimestamp(int(time_stamp))
        eth_value = Decimal(value)/Decimal(1000000000000000000)
        writer.writerow(["success", transaction_id, tx_from,
                        tx_to, value, eth_value, time_stamp, date_object])
        print(index)
        print(transaction_id)
        get_transaction_detail.get_transaction_detail(
            transaction, index, address, platform_name)

    f_list.close()
