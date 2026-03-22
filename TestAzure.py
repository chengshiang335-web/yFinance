import yfinance as yf   
import stock_service
import db_service


info = stock_service.tickerInfo("2330.TW")
print(info)

db_service.insert_to_db(
    info.get("symbol", "2330.TW"), 
    info.get("shortName"), 
    info.get("open"), 
    info.get("dayHigh"), 
    info.get("dayLow"), 
    info.get("currentPrice")
)


