URL = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion'
with open("key.txt", "r") as reading:
    KEY = reading.read()
HEADER = {"X-CMC_PRO_API_KEY": KEY}
PARAMS = {"amount": 1, "symbol": "KAS"}
reading.close()
