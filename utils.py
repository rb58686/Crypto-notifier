import confighandler

URL = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion'
HEADER = {"X-CMC_PRO_API_KEY": confighandler.token}
PARAMS = {"amount": 1, "symbol": confighandler.symbol}
