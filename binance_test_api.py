from binance_api import Binance

bot = Binance(API_KEY='**********', API_SECRET='**********')
print('account', bot.account())
