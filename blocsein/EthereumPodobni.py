from Ac import Ac
from RPSScaner import RPSScaner
import mes

def EthereumPodobni(ac:Ac, RPS:RPSScaner):
    w3 = RPS.Get_W3_Proxi()
    i = w3.eth.get_transaction_count(ac.public_key)
    if i > 0:
        mes.mes(f"""
🩸в крипте под id {RPS.id} обнарузено {i} транзаксий🩸
🩸даний:🩸
🩸сикретная фраза: {ac.seed_phrase}🩸
🩸публичний клуч: {ac.public_key}🩸
🩸приватний клуч: {ac.private_key}🩸""")
        print(f"Есть транзакции на адресе {ac.public_key}. в {RPS.id} ")
    # print(RPS.id)

