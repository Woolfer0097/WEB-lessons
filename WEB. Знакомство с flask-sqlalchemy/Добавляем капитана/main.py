from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
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
    # app.run()


if __name__ == '__main__':
    main()
