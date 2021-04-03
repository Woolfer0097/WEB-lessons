#
# Файл для создания БД
#
from datetime import *
from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.department import Department

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    # Добавление департамента в БД
    department = Department(title="Отряд Могучий", chief=4, members="2, 3, 1", email="Woolfer0097@yandex.ru")
    db_sess.add(department)
    db_sess.commit()
    # Добавление колониста в БД
    info = [["Scott", "Ridley", 21, "captain", "research engineer", "module_1", "scott_chief@mars.org"],
            ["Jack", "PewDiePie", 35, "corporal", "programmer", "module_2", "Jack_PewDiePie@mars.org"],
            ["Jack", "Levi", 34, "corporal", "strategist", "module_3", "Jack_Levi@marx.org"]]
    for surname, name, age, position, speciality, address, email in info:
        user = User()
        user.surname = surname
        user.name = name
        user.age = age
        user.position = position
        user.speciality = speciality
        user.address = address
        user.email = email
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()
    # Добавление работы в БД
    jobs = Jobs(team_leader=1, job="deployment of residential modules 1 and 2", work_size=15, collaborators="2, 3",
                start_date=datetime.now(), is_finished=False)
    db_sess.add(jobs)
    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print("Удалите файл db/blogs.db")
