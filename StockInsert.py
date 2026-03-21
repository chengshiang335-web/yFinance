import datetime

import yfinance as yf
import pymssql

import time

#今日行情與指數
def ticker_summary(id):
    tick = yf.Ticker(id)
    info = tick.fast_info
    #print(info) 

    print(f'開盤:{info.open}')
    print(f'今日最高:{info.day_high}')
    print(f'今日最低:{info.day_low}')
    print(f'目前價格:{info.last_price}')
    return info



"""
使用 pymssql 對資料庫進行連接
"""
server = "hsiangdb.database.windows.net"
database = "hsiangDB1"
user = "chengshiang"
password = "Tools335~"  
'''密碼洩漏問題'''

INS_SQL = """
    INSERT into dbo.StockPrice(StockId,sName, OpenPrice, HighPrice, LowPrice, ClosePrice) 
    VALUES (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
    )
"""
try:
    connect = pymssql.connect(server, user, password, database)
    cursor = connect.cursor()

    print("資料庫連線成功")


    info = ticker_summary("2330.TW")
    cursor.execute(INS_SQL, ("2330", "台積電", info.open, info.day_high, info.day_low, info.last_price))
    # pymssql 預設設定 autocommit = false
    connect.commit()

    print("資料寫入完畢")
    cursor.close()
    connect.close()


except Exception as e: 
    print(f'連線失敗: 原因{e}')
