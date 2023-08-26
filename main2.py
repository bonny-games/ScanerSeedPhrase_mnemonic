import threading
import time

from web3 import Web3
from web3.middleware import geth_poa_middleware
w3 = Web3(Web3.HTTPProvider("https://eth.llamarpc.com"))

private_key = "0x8b621dd0bc1c74feaf24ffdfd27ffeedf4e562f944a8eb5dafee9798971967e1"
pub_key = "0xC3ff7f3062600c610842432755e0Dc1FF09B4443"

w3.middleware_onion.inject(geth_poa_middleware, layer=0)

recipient_pub_key = "0x9dAC9810cec7b6B7957159158f1dEE8a61e40Bc8"


# while(True):
#     balance = w3.eth.get_balance(pub_key)
#     print("balance: "+str(balance))
#     time.sleep(5)


balance = w3.eth.get_balance(pub_key)

print()
print("Nou: mempul")
print("balance: " + str(balance))
gasPrice = w3.eth.gas_price
gasLimit = 21000
print("gasPrice: " + str(gasPrice))
print("gasLimit: " + str(gasLimit))
print("value: " + str(balance-gasLimit*gasPrice))
nonce = w3.eth.get_transaction_count(pub_key)
tx = {
    'nonce': nonce,
    'to': recipient_pub_key,
    'value': balance-gasLimit*gasPrice,
    'gas': gasLimit,
    'gasPrice': gasPrice
}

signed_tx = w3.eth.account.sign_transaction(tx, private_key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
print(w3.toHex(tx_hash))


