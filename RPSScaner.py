import requests
from bs4 import BeautifulSoup
import json

from web3 import Web3
import random
import Proxi


class RPSScaner:
    listUrl = None
    zapros = 0

    def __init__(self, id):
        self.id = id
        r = requests.get(f"https://chainlist.org/chain/{id}")
        html = BeautifulSoup(r.content, "html.parser")
        e = html.select("#__NEXT_DATA__")
        res = json.loads(e[0].text)
        listUrls = []
        for i in res["props"]["pageProps"]["chain"]["rpc"]:
            url = i["url"]
            w3 = Web3(Web3.HTTPProvider(url))
            # print(url)
            try:
                w3.isConnected()
                listUrls.append(url)
                # print("RPC-сервер доступен")
            except:
                pass
                # print("Не удалось подключиться к RPC-серверу")
        self.listUrl = listUrls

    def Get_RPC_url(self, i=-1) -> str:
        if i == -1:
            # if(len(self.listUrl)<1):
            #     return self.__init__(self.id)
            self.zapros += 1
            if(self.zapros%100_000):
                self.__init__(self.id)
            return self.listUrl[random.randint(0, len(self.listUrl)-1)]
        return self.listUrl[i % len(self.listUrl)]

    def Get_W3(self) -> Web3:
        def podFun():
            url = self.Get_RPC_url()
            w3 = Web3(Web3.HTTPProvider(url))
            return w3

        w3 = podFun()
        while True:
            try:
                connected = w3.isConnected()
                if connected:
                    break
            except:
                pass
            # self.listUrl.remove(w3.provider.endpoint_uri)
            # if len(self.listUrl)<2:
            #     self.__init__(self.id)
            w3 = podFun()
        return w3

    def Get_W3_Proxi(self) -> Web3:
        def podFun():
            proxies = Proxi.procs.GetProxi()
            if(proxies == None):
                return self.Get_W3()
            session = requests.Session()
            session.proxies.update(proxies)

            w3 = Web3(Web3.HTTPProvider(self.Get_RPC_url(), session=session))
            return w3

        w3 = podFun()
        while True:
            try:
                connected = w3.isConnected()
                if connected:
                    break
            except:
                pass
            # self.listUrl.remove(w3.provider.endpoint_uri)
            # if len(self.listUrl)<2:
            #     self.__init__(self.id)
            w3 = podFun()

        return w3

RPC_Ethereum_Mainnet = None
RPC_Binance_Smart_Chain_Mainnet = None
RPC_Arbitrum_One = None
RPC_Polygon_Mainnet = None


# RPC = RPSScaner(1)
# RPC = RPSScaner(1)

# r = 0
# for i in range(1000):
#     w3 = RPC.Get_W3_Proxi()
#     print(i)
#     try:
#         if not w3.isConnected():
#             r +=1
#     except:
#         r += 1
# print(f"{r}/{i+1}")