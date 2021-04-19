from flask import Flask, render_template, redirect, abort, request, url_for
from data import db_session
from data.users import User
from data.book import Book
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from forms.login import LoginForm
from forms.register import RegisterForm
from forms.change_password import ChangePasswordForm

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
        user = db_sess.query(User).filter((User.email == form.email.data) | (User.nickname == form.email.data)).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/main_page")
        return render_template('login_page.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template("login_page.html", title="Авторизация", form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    db_sess = db_session.create_session()
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register_page.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register_page.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            email=form.email.data,
            nickname=form.login.data,
            age=form.age.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect("/login")
    return render_template('register_page.html', title='Регистрация', form=form)


@app.route("/main_page")
def main_page():
    return render_template("main_page.html", title="Главная страница")


@app.route("/personal_account")
@login_required
def personal_account():
    return render_template("personal_account_page.html", title="Личный кабинет")


@app.route("/change_avatar", methods=["GET", "POST"])
@login_required
def change_avatar():
    db_sess = db_session.create_session()
    if request.method == "POST":
        file = request.files['file']
        with open(f"static/images/avatars/{current_user.nickname}.png", "wb") as file_write:
            file_write.write(file.read())
        user = db_sess.query(User).filter(User.id == current_user.id).first()
        user.user_avatar = f"{current_user.nickname}.png"
        db_sess.commit()
        return redirect("/change_avatar")
    else:
        return render_template("change_avatar_page.html", title="Смена аватара")


@app.route("/")
def index():
    return render_template("editor.html", title="Редактор")


@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    db_sess = db_session.create_session()
    form = ChangePasswordForm()
    if request.method == "POST":
        if current_user.check_password(form.old_password.data):
            current_user.set_password(form.password.data)
            db_sess.merge(current_user)
            db_sess.commit()
            return redirect("/personal_account")
        else:
            return render_template("change_password_page.html", title="Смена пароля", form=form,
                                   message="Неправильный пароль")
    else:
        return render_template("change_password_page.html", title="Смена пароля", form=form)


@app.route("/edit_book/<int:book_id>")
@login_required
def edit_book(book_id):
    pass


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/main_page")


if __name__ == '__main__':
    db_session.global_init("db/books.db")
    app.run(port=8080, host='127.0.0.1')
