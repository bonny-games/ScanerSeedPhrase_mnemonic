import os
import concurrent.futures
import requests

import new

from bip_utils import Bip32Slip10Secp256k1,Bip39SeedGenerator,TrxAddrEncoder


def get_address_from_seed(seed):
    seed_bytes = Bip39SeedGenerator(seed).Generate()
    bip32_mst_ctx = Bip32Slip10Secp256k1.FromSeed(seed_bytes)
    bip32_der_ctx = bip32_mst_ctx.DerivePath("m/44'/195'/0'/0/0")
    tron_address = TrxAddrEncoder.EncodeKey(bip32_der_ctx.PublicKey().KeyObject())
    return tron_address

def get_private_key_from_seed(seed):
    seed_bytes = Bip39SeedGenerator(seed).Generate()
    bip32_mst_ctx = Bip32Slip10Secp256k1.FromSeed(seed_bytes)
    bip32_der_ctx = bip32_mst_ctx.DerivePath("m/44'/195'/0'/0/0")
    private_key = bip32_der_ctx.PrivateKey().KeyObject().Raw()
    return str(private_key)

sedd = "auto basket quality dash pole myself mimic bright next mammal avoid prevent"
print(get_address_from_seed(sedd))
print(get_private_key_from_seed(sedd))
exit()


# Function to check USDT TRC20 balance for a given wallet
def check_usdt_balance(seed_phrase):
    try:
        address = get_address_from_seed(seed_phrase)
        url = f"https://apilist.tronscan.org/api/account?address={address}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for token in data['tokens']:
                if token['tokenId'] == 'TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t':  # USDT tokenId on Tron network
                    result = "{}:{}\n".format(seed_phrase,token['balance'])
                    print(result)
                    f=open('result.txt','a+')
                    f.write(result)
                    return result
    except:
        print(seed_phrase, "/wallet empty/")
        pass
    else:
        print(seed_phrase, "/inalid phrase/")
        pass
    return
        


# Function to check USDT TRC20 balance for a list of wallets
def check_wallets(seed_phrases):
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
        futures = [executor.submit(check_usdt_balance, seed_phrase) for seed_phrase in seed_phrases]
        for future in concurrent.futures.as_completed(futures):
            if future.result():
                results.append(future.result())
    return results


# Loop through all the files with seed phrases
# file_number = 0
# while True:
#     file_name = f"comb{file_number}.txt"
#     if os.path.isfile(file_name):
#         with open(file_name, "r") as f:
#             seed_phrases = [line.strip() for line in f]
#
#         # Check USDT TRC20 balance for each wallet
#         results = check_wallets(seed_phrases)
#
#     # Move on to the next file
#     file_number += 1
#     print(file_name)

while True:
    results = check_wallets(new.word_generator())
