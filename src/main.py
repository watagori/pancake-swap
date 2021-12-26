'''get lists and details of transactin by any address'''
import get_transaction_list

TRANSACTION_NUMBER = 10
TRANSACTION_ADDRESS = "0x05fF2B0DB69458A0750badebc4f9e13aDd608C7F"  # wakimoto-san
# TRANSACTION_ADDRESS= "0x10b02dC3df82f53c0C453f3639211f769cD36cfe" #panckake only
PLATFORM_NAME = "PancakeSwap"

get_transaction_list.get_transaction_by_address(
    str.lower(TRANSACTION_ADDRESS), TRANSACTION_NUMBER, PLATFORM_NAME)
