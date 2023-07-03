from .EthereumPodobni import EthereumPodobni
from .Tron import Tron
from RPSScaner import *
import RPSScaner
from threading import Thread
import mes

index = 0

def startBlokceins(AC):
    global index
    index += 1

    print(f"{AC.public_key}   обработано: {index}")
    if(index%100==0):
        mes.mes(f"обработано: {index}")

    Ethereum_Mainnet = Thread(target=EthereumPodobni, args=(AC, RPSScaner.RPC_Ethereum_Mainnet))
    Binance_Smart_Chain_Mainnet = Thread(target=EthereumPodobni, args=(AC, RPSScaner.RPC_Binance_Smart_Chain_Mainnet))
    Arbitrum_One = Thread(target=EthereumPodobni, args=(AC, RPSScaner.RPC_Arbitrum_One))
    Polygon_Mainnet = Thread(target=EthereumPodobni, args=(AC, RPSScaner.RPC_Polygon_Mainnet))
    TronPotok = Thread(target=Tron, args=(AC,))

    Ethereum_Mainnet.start()
    Binance_Smart_Chain_Mainnet.start()
    Arbitrum_One.start()
    Polygon_Mainnet.start()
    TronPotok.start()

    Ethereum_Mainnet.join()
    Binance_Smart_Chain_Mainnet.join()
    Arbitrum_One.join()
    Polygon_Mainnet.join()
    TronPotok.join()

    # EthereumPodobni(AC, RPC_Ethereum_Mainnet)
    # Tron(AC)
    # EthereumPodobni(AC, RPC_Binance_Smart_Chain_Mainnet)
    # EthereumPodobni(AC, RPC_Arbitrum_One)
    # EthereumPodobni(AC, RPC_Polygon_Mainnet)
