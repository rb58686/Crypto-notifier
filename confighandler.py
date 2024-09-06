import configparser

config = configparser.ConfigParser()
config.read("config.ini")

symbol = config.get('symbol', 'symbol')
amount = config.getfloat('amount', 'amount')
token = config.get('token', 'cmc_token')


