from flask import Flask, render_template, redirect, abort, request
from data import db_session
from data.users import User
from data.book import Book
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from forms.login import LoginForm
from forms.register import RegisterForm
from forms.job import JobForm
from data.users_resource import UsersListResource, UsersResource

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template("login.html", title="Авторизация", form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    db_sess = db_session.create_session()
    form = RegisterForm()
    user_resource = UsersListResource()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user_resource.post(json={'nickname': form.nickname.data, })
        return redirect("/login")
    return render_template('register.html', title='Регистрация', form=form)


@app.route("/")
def index():
    return render_template("main_page.html", title="Главная страница")


@app.route("/")
def main_page():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        user = db_sess.query(User).filter(User.id == Book.team_leader).first()
        jobs = db_sess.query(Book).filter(Book.team_leader == current_user.id).all()
        data = [{'id': job.id, 'team_leader': user.nickname, 'job': job.job,
                 'work_size': job.work_size, 'collaborators': job.collaborators, 'is_finished': job.is_finished}
                for job in jobs]
        return render_template("main_page.html", title="Главная страница", data=data, job_flag=True)





@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')
