import datetime
import schedule


def job():
    n = datetime.datetime.now().hour % 12
    if n == 0:
        n = 12
    for i in range(n):
        print("Ку")


schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()
