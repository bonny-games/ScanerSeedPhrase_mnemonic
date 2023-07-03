import sys
from cx_Freeze import setup, Executable

# Путь к вашему файлу main.py
main_script = 'main.py'

# Создание исполняемого файла
executables = [Executable(main_script)]

# Определение скрытых импортов
hidden_imports = [
    'aiohttp', 'aiosignal', 'altgraph', 'asn1crypto', 'async_timeout',
    'attrdict', 'attrs', 'base58', 'beautifulsoup4', 'bip_utils', 'bip39',
    'bitarray', 'bs4', 'cbor2', 'certifi', 'cffi', 'charset_normalizer',
    'coincurve', 'crcmod', 'cryptography', 'cytoolz', 'ecdsa',
    'ed25519_blake2b', 'eth_abi', 'eth_account', 'eth_hash', 'eth_keyfile',
    'eth_keys', 'eth_rlp', 'eth_typing', 'eth_utils', 'frozenlist', 'hexbytes',
    'idna', 'ipfshttpclient', 'jsonschema', 'lru', 'multiaddr', 'multidict',
    'my_fake_useragent', 'netaddr', 'parsimonious', 'pefile', 'protobuf',
    'py_sr25519_bindings', 'pybip39', 'pycparser', 'pycryptodome', 'PyNaCl',
    'pyrsistent', 'pyTelegramBotAPI', 'regex', 'requests', 'rlp', 'six',
    'soupsieve', 'telebot', 'toolz', 'urllib3', 'varint', 'web3', 'websockets',
    'yarl', 'cytoolz._signatures',
]

# Опции сборки
build_options = {
    'packages': [],
    'excludes': [],
    'include_files': [],
    'include_msvcr': True
}

# Конфигурация сборки
setup(
    name='MyApp',
    version='1.0',
    description='My Application',
    options={'build_exe': build_options},
    executables=executables
)
