from pybip39 import Mnemonic, Seed
from datetime import datetime
from web3.auto import w3
from web3 import Web3
from eth_account import Account
import hashlib
from bip_utils import Bip32Slip10Secp256k1, Bip39SeedGenerator, TrxAddrEncoder


class Ac:
    memonici: Mnemonic = None
    seed_phrase: str = None

    def __init__(self):
        self.memonici = Mnemonic()
        self.seed_phrase = str(self.memonici)

    _public_key = None

    @property
    def public_key(self):
        if (self._public_key != None):
            return self._public_key
        self._public_key = w3.eth.account.privateKeyToAccount(self.private_key).address
        return self._public_key

    _private_key = None

    @property
    def private_key(self):
        if (self._private_key != None):
            return self._private_key
        mnemonic = " ".join(self.seed_phrase.split())
        self._private_key = Account.from_mnemonic(mnemonic)._private_key.hex()
        return self._private_key

    _public_key_Tron = None

    @property
    def public_key_Tron(self):
        if (self._public_key_Tron != None):
            return self._public_key_Tron
        seed_bytes = Bip39SeedGenerator(self.seed_phrase).Generate()
        bip32_mst_ctx = Bip32Slip10Secp256k1.FromSeed(seed_bytes)
        bip32_der_ctx = bip32_mst_ctx.DerivePath("m/44'/195'/0'/0/0")
        tron_address = TrxAddrEncoder.EncodeKey(bip32_der_ctx.PublicKey().KeyObject())
        self._public_key_Tron = tron_address
        return tron_address

    _private_key_Tron = None

    @property
    def private_key_Tron(self):
        if (self._private_key_Tron != None):
            return self._private_key_Tron
        seed_bytes = Bip39SeedGenerator(self.seed_phrase).Generate()
        bip32_mst_ctx = Bip32Slip10Secp256k1.FromSeed(seed_bytes)
        bip32_der_ctx = bip32_mst_ctx.DerivePath("m/44'/195'/0'/0/0")
        private_key = bip32_der_ctx.PrivateKey().KeyObject().Raw()
        self._private_key_Tron = str(private_key)
        return self._private_key_Tron
