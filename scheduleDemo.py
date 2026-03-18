import schedule
import time
from datetime import datetime


def run_every_5seconds():
    print(f"每 5秒執行一次")
    
def run_every_60seconds():
    print(f"每 60秒執行一次")

def run_at_spec_time():
    now= datetime.now()
    print(f"觸發時間: {now}")

def run_and_cancelJob():
    # 本任務視情況 決定是否繼續執行, 例如各分點的檔案在營業結束後要上傳 pos csv file
    # schedule 沒有提供設定開始的邏輯 , 必須在 func內自己判斷時間是否滿足開始執行
    global showcount
    showcount += 1
    print(f"每 2秒執行一次, showcount={showcount}")


    if( showcount>2 ):
        print("任務完成, 不再繼續執行")
        #schedule.clear()  #清除所有任務
        #schedule.cancel_job(myJob)   #通知 schedule 不用再安排後續的任務了
        #return schedule.cancel_job


showcount = 0

#只是安排一個任務 
# schedule.every(5).seconds.do(run_every_5seconds)
# schedule.every(1).minutes.do(run_every_60seconds)
# schedule.every().day.at("14:06").do(run_at_spec_time)
# schedule.every().hours.at(":31").do()
# schedule.every().friday.at("16:30").do()

# 設定結束或取消的方式
#schedule.every(30).seconds.do(run_every_5seconds).until("13:30")  # 開始每30秒執行任務直到 13:30 結束
#myJob = schedule.every(2).seconds.do(run_and_cancelJob)   # 一旦檔案下載完成 自動結束

def ticker_history(id):
    # 取得歷史資料
    tick = schedule.Ticker(id)
    hist = tick.history(period="3d")    
    print(hist)



ticker_history("2330.TW")

# while True:
#     #要求 schedule 每n單位 檢查一次是否有任務需要執行
#     schedule.run_pending()
#     time.sleep(1) 