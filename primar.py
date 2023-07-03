

from pybip39 import Mnemonic, Seed
# for i in range(100):
#     print(Mnemonic())
for i in range(0):
    mnemonic = Mnemonic()
    # Get the phrase
    phrase = mnemonic.phrase
    print(f"phrase: {phrase}")
    # Get the HD wallet seed
    seed = Seed(mnemonic, "")
    # get the HD wallet seed as raw bytes
    seed_bytes = bytes(seed)
    print(seed_bytes)
from datetime import datetime
from web3.auto import w3
from web3 import Web3
from eth_account import Account
Account.enable_unaudited_hdwallet_features()
start_time = datetime.now()

W3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/df1dd05f17fe4a43bc634e80570b774a"))

def generate_ethereum_keys_from_seed(seed_phrase):
    # Получите 12 слов seed-фразы и преобразуйте их в мнемоническую фразу
    mnemonic = " ".join(seed_phrase.split())

    # Генерация приватного ключа из seed-фразы
    private_key = Account.from_mnemonic(mnemonic)._private_key.hex()

    # Получение публичного ключа из приватного ключа
    public_key = w3.eth.account.privateKeyToAccount(private_key).address

    return private_key, public_key

seed_phrase = str(Mnemonic())
import hashlib
# Входные данные для хеширования
data = seed_phrase

# Создание объекта SHA-256
sha256_hash = hashlib.sha256()

# Обновление хэша данными
sha256_hash.update(data.encode('utf-8'))

# Получение итогового хэша
hashed_data = sha256_hash.hexdigest()

# Вывод хэша
print(hashed_data)

_private_key, _public_key = generate_ethereum_keys_from_seed(seed_phrase)


print("seed phrase: ", seed_phrase)
print("Приватный ключ: ", _private_key)
print("Публичный ключ: ", _public_key)
print("balans: ", W3.eth.get_balance(_public_key))
print()




print(datetime.now() - start_time)
# import binascii
# import os
# from bip39 import bip39,cli_encode
#
# # Генерация мнемонической фразы
# # entropy = binascii.hexlify(os.urandom(16)).decode()
# # mnemonic_words = mnemonic.from_entropy(entropy)
# mnemonic_words = cli_encode("12")
# print("Мнемоническая фраза:", ' '.join(mnemonic_words))
#
# # Создание семени из мнемонической фразы
# seed = bip39.mnemonic_to_seed(mnemonic_words)
#
# # Получение приватного ключа
# private_key = bip39.generate_private_key(seed)
# print("Приватный ключ:", private_key)







from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

# Генерируем приватный ключ
# private_key = ec.generate_private_key(ec.SECP256K1())
#
# # Получаем публичный ключ из приватного
# public_key = private_key.public_key()
#
# # Сериализуем приватный и публичный ключи в PEM формат
# private_pem = private_key.private_bytes(
#     encoding=serialization.Encoding.PEM,
#     format=serialization.PrivateFormat.PKCS8,
#     encryption_algorithm=serialization.NoEncryption()
# )
# public_pem = public_key.public_bytes(
#     encoding=serialization.Encoding.PEM,
#     format=serialization.PublicFormat.SubjectPublicKeyInfo
# )
#
# # Выводим результат
# print("Секретный ключ:")
# print(private_pem.decode())
# print("Публичный ключ:")
# print(public_pem.decode())
# exit()
# from eth_keyfile import create_keyfile_json, decode_keyfile_json
# from eth_utils import decode_hex
#
# import hashlib
#
#
# # Ваша секретная фраза (мнемоническая фраза)
# mnemonic_phrase = "consider mule equip system stumble course mad oppose private stumble raven mix"
#
# # Генерация ключей из секретной фразы
# keyfile_json = create_keyfile_json(mnemonic_phrase)
#
# # Декодирование ключей из JSON
# decoded_key = decode_keyfile_json(keyfile_json)
#
# # Получение секретного и публичного ключей
# private_key = decode_hex(decoded_key['private_key'])
# public_key = decode_hex(decoded_key['public_key'])
#
# # Вывод результатов
# print("Секретный ключ (hex):", private_key.hex())
# print("Публичный ключ (hex):", public_key.hex())




# import requests
# from threading import Thread
#
# i = 0
# def start():
#     global i
#     while True:
#         print(i)
#         try:
#             requests.get("https://apilist.tronscan.org/api/account?address=0x9dAC9810cec7b6B7957159158f1dEE8a61e40Bc8")
#         except:
#             print("fines")
#             exit()
#         i+=1
#
#
# for _ in range(100):
#     Thread(target=start, daemon=True).start()
# print("f")







