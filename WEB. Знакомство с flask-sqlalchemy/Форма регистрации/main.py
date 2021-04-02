from flask import Flask, render_template, request
from data import db_session
from data.users import User
from forms.user import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == "GET":
        form = RegisterForm()
        return render_template('register.html', form=form)
    elif request.method == "POST":
        db_session.global_init("db/blogs.db")
        user = User()
        db_sess = db_session.create_session()
        user.email = request.form["email"]
        user.password = request.form["password"]
        user.surname = request.form["surname"]
        user.name = request.form["name"]
        user.age = request.form["age"]
        user.position = request.form["position"]
        user.speciality = request.form["speciality"]
        user.address = request.form["address"]
        db_sess.add(user)
        db_sess.commit()
        return "Success"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
