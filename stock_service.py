import yfinance as yf

#今日行情與指數
def tickerFastInfo(id):
    tick = yf.Ticker(id)
    info = tick.fast_info
    print(f'開盤:{info.open}')
    print(f'今日最高:{info.day_high}')
    print(f'今日最低:{info.day_low}')
    print(f'目前價格:{info.last_price}')
    return info

def tickerInfo(id):
    tick = yf.Ticker(id)
    info = tick.info
  
    info.symbol
    print(f'公司:{ info.get("shortName")}')
    print(f'開盤:{info.get("open")}')
    print(f'今日最高:{info.get("dayHigh")}')
    print(f'今日最低:{info.get("dayLow")}')
    print(f'目前價格:{info.get("currentPrice")}')
    return info