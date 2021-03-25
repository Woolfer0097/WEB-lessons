import datetime
import schedule

message = input("Какое сообщение вы хотите выводить каждый час? ")
t = input("В какое время вас не стоит беспокоить?\nФормат ввода 00-0ЧАС ")
time = datetime.datetime.strptime(t, "00-%H")
running = True


def job():
    if time.hour < datetime.datetime.now().hour < 0:
        for i in range(datetime.datetime.now().hour % 12):
            print(message)


schedule.every().hour.do(job)

while running:
    schedule.run_pending()
