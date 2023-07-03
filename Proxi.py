import random
from threading import Thread
import requests, json, time
from my_fake_useragent import UserAgent as UA

ua = UA(family='chrome')
UserAgents = ua.random()
import config


def arxiv():
    """достает все дати в нутри архива"""
    r = requests.get("https://checkerproxy.net/api/archive/")
    u = json.loads(r.text)
    mas = []
    for i in u:
        mas.append(i["date"])
    return mas


path = "Proxi.txt"


class Proxi:
    """достает рабочий прокси"""
    proxiList = []
    heid = {
        'User-Agent': UserAgents
    }
    id = 0
    gotovo = False

    def __init__(self):
        self.Updeit()

    def Dowload(self, rasir=False):
        """скачаивает прокси со саита"""
        r = arxiv()[::-1][10:] if rasir else list(set(arxiv()))[::-1][:10]
        mas = []
        index = 0

        # eroor1 =0
        # eroor2 = 0
        # eroorscan = 0

        for i in r:
            mas2 = []
            # print(f"w{i}")
            r = requests.get("https://checkerproxy.net/api/archive/" + str(i))
            try:
                u = json.loads(r.text)
            except:
                print(r.text)
                raise
            # for item in u:
            #
            #
            #     if (not item["type"] == 2):
            #         eroor1 += 1
            #     if (not item["timeout"] < 4000):
            #         eroor2 += 1
            #     eroorscan +=1
            #
            #
            #     if item["type"] == 2 and item["timeout"] < 4000:
            #         mas2.append(item["addr"])
            mas2 = [item["addr"] for item in u if item["type"] == 2 and item["timeout"] < 4000]

            mas.append(mas2)
            index += 1

            # print(f"index: {index}")

        for i in range(index):
            self.proxiList += mas[i]

        # print(f"len: {len(self.proxiList)}")
        # print("Eroor")
        # print(eroor1/eroorscan)
        # print(eroor2/eroorscan)
        # print(len(self.proxiList))

    def Updeit(self):
        """обновляет работа способность прокси"""
        try:
            proxi = ""
            with open(path, 'r', encoding="utf-8") as f:
                proxi += f.read()
            self.proxiList = proxi.split("\n")
            if len(self.proxiList) <= config.minimumProcsis:
                self.Dowload()
        except:
            self.Dowload()

        self.__TestGlobalMulti()
        if len(self.proxiList) <= config.minimumProcsis:
            print("Procsis Malo")
            self.Dowload(True)
            self.__TestGlobalMulti()

        print("Proxi ок N: " + str(len(self.proxiList)))
        with open(path, 'w', encoding="utf-8") as f:
            f.write("\n".join(self.proxiList))

    def __TestGlobal(self):
        """тест прокси"""
        for i in range(len(self.proxiList)):
            self.__TestLocal(i)
            # print(f"{i}/{len(self.proxiList)}   {i / len(self.proxiList) * 100}%")

        for i in range(0, len(self.proxiList), -1):
            if self.proxiList[i] == None:
                del self.proxiList[i]

    def __TestGlobalMulti(self):
        """тестирования прокси в много потоке"""
        self.proxiList = list(set(self.proxiList))
        pot = config.PotocProcsis
        pot2 = pot * 2
        potoc = {}

        lens = (len(self.proxiList) // pot * pot)
        for i in range(len(self.proxiList) - lens):
            Thread(target=self.__TestLocal, args=(i + lens - 1,)).start()

        # time.sleep(3)

        ii = 0
        vitsotekOld=0
        for i in range(lens * 2):

            vitsotek = (i + 1) / (lens * 2) * 100
            if(int(vitsotek)!=vitsotekOld):
                vitsotekOld=int(vitsotek)
                print(f"Procsi Operasions: {int(vitsotek)}%")

            if i % pot2 - pot >= 0:
                p = potoc[(pot - (i % pot2 - pot)) - 1 - (i // (pot * 2))]
                p["pot"].join()
                # print(f"{p['i']}/{lens-1}   {p['i'] / (lens-1) * 100}%")
            else:
                t = Thread(target=self.__TestLocal, args=(ii,))
                t.start()
                potoc[-(i % pot2 - pot) - 1 - (i // (pot * 2))] = {"pot": t, "i": ii}
                ii += 1
        lens = len(self.proxiList)
        time.sleep(5)
        for i in range(0, lens):
            i = lens - i - 1
            if self.proxiList[i] == None or self.proxiList[i] == '' or self.proxiList[i] == ' ':
                del self.proxiList[i]

    def __TestLocal(self, i: int):
        """тестирует конкретний прокси"""
        # print(prox)
        try:
            r = requests.get(url="https://www.google.com/",
                             proxies={'https': self.proxiList[i]},
                             headers=self.heid,
                             timeout=2)
            if r.status_code == 200:
                # print(f"Proxi ок: {self.proxiList[i]}")
                return
            self.proxiList[i] = None
        except:
            try:
                self.proxiList[i] = None
            except:
                pass

    def GetProxi(self):
        """получить конкретний прокси"""
        if random.randint(0, int(len(self.proxiList) / 5) + 3) == 0:
            return None
        if len(self.proxiList) == 0 and self.id > 2_000_000*(len(self.proxiList)/config.minimumProcsis):
            self.id = 0
            self.Updeit()
            return None
        elif len(self.proxiList) == 1:
            nar = self.proxiList[0]
        else:
            nar = self.proxiList[self.id % len(self.proxiList)]
        self.id += 1
        return {'https': nar}


procs = None
