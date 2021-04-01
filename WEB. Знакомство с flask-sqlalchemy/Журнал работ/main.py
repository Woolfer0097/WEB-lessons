from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    data = []
    for job in db_sess.query(Jobs).all():
        for user in db_sess.query(User).filter(User.id == job.team_leader):
            full_name = f"{user.surname} {user.name}"
            data.append([job.job, full_name, job.work_size, job.collaborators, job.is_finished])
    return render_template('journal.html', data=data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
