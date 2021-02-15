import schedule
import time
import src.core.configParse

data = src.core.configParse.parse("0 0 0 0 0 echo hi")


def job():
    print("Command running: " + data["command"])


schedule.every(int(data["minute"])).minute.do(job)
schedule.every(int(data["hour"])).hour.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
