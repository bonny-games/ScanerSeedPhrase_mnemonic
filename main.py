import requests
from eth_account import Account

Account.enable_unaudited_hdwallet_features()
from threading import Thread
import config
from Ac import Ac
import blocsein
import mes
import Proxi
import RPSScaner
from datetime import datetime

i = 0
timeStart = datetime.now()

def AcStartSpidTest():
    global i
    ac = Ac()
    t = ac.public_key
    i += 1
    if(i>1_000):
        print(datetime.now()-timeStart)
        print(i)
        exit()


def AcStart():
    ac = Ac()
    blocsein.startBlokceins(ac)


def main():
    while True:
        AcStart()


if __name__ == '__main__':
    response = requests.get('https://api.ipify.org/?format=json')
    data = response.json()
    ip = data['ip']
    mes.mes(f"P_Start: {ip}")

    print("Proxi Start")
    Proxi.procs = Proxi.Proxi()
    print("Proxi fines")

    print("Rpc Scan Start")
    RPSScaner.RPC_Ethereum_Mainnet = RPSScaner.RPSScaner(1)
    RPSScaner.RPC_Binance_Smart_Chain_Mainnet = RPSScaner.RPSScaner(56)
    RPSScaner.RPC_Arbitrum_One = RPSScaner.RPSScaner(42161)
    RPSScaner.RPC_Polygon_Mainnet = RPSScaner.RPSScaner(137)
    print("Rpc Scan fines")

    mes.mes(f"Start: {ip}")
    for _ in range(config.MultiPotoc):
        Thread(target=main).start()
