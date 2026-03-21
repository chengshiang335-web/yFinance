import schedule
import time
from datetime import datetime

 
def job():
    print("正在執行週一至週五 13:31 的任務...")

# 定義要執行的星期屬性清單
weekdays = [

    schedule.every().saturday,

    schedule.every().monday,
    schedule.every().tuesday,
    schedule.every().wednesday,
    schedule.every().thursday,
    schedule.every().friday
]


def job():
    print("正在執行週一至週五 13:31 的任務...")

# 批次設定執行時間與任務函式
#for day in weekdays:
    #day.at("13:31:00").do(job)
    #day.minute.at("31").do(job)  # 每小時的31分執行一次

schedule.every().minute.at(":00").do(job)  # 每小時的31分執行一次

while True:
    #要求 schedule 每n單位 檢查一次是否有任務需要執行
    schedule.run_pending()
    time.sleep(1) 