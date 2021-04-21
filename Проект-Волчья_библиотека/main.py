from flask import Flask, render_template, redirect, abort, request, url_for
from datetime import datetime
from data import db_session
from data.users import User
from data.book import Book
from data.genres import Genre
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from forms.login import LoginForm
from forms.register import RegisterForm
from forms.edit_book import EditBookForm
from forms.change_password import ChangePasswordForm
import os, random

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


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


@app.route("/main_page")
def main_page():
    db_sess = db_session.create_session()
    books = db_sess.query(Book).all()
    return render_template("main_page.html", title="Главная страница", books=books)


@app.route("/")
def index():
    return render_template("writer-page.html")


@app.route("/personal_account")
@login_required
def personal_account():
    db_sess = db_session.create_session()
    user_books = db_sess.query(Book).filter(Book.user_id == current_user.id).all()
    return render_template("personal_account_page.html", books=user_books)


@app.route("/show_book/<int:book_id>")
def show_book(book_id):
    db_sess = db_session.create_session()
    book = db_sess.query(Book).filter(Book.id == book_id).first()
    content_analysis = book.content_analysis
    l_u = book.updated_date
    image = book.image_link
    if not image or not os.path.exists(image):
        image = "static/images/skins/standard-image.jpg"
    return render_template("book_info_page.html",
                           title=book.title, image=image, author=book.book_author, genre=book.genre.title,
                           user_author=book.user.nickname, content_analysis=content_analysis, last_update=l_u)


@app.route("/edit_book/<int:book_id>", methods=["GET", "POST"])
@login_required
def edit_book(book_id):
    form = EditBookForm()
    db_sess = db_session.create_session()
    book = db_sess.query(Book).filter(Book.id == book_id).first()
    if not book:
        abort(404, message="Такой книги не существует")
    if request.method == "POST":
        book.title = form.title.data
        book.book_author = form.book_author.data
        book.genre_id = form.genre.data
        book.updated_date = datetime.now()
        book.content_analysis = request.form['text']
        file = request.files['file']
        image_link = f"static/images/skins/{book.title}-{random.randint(1, 100000)}.png"
        os.remove(book.image_link)
        with open(f"{image_link}", "wb") as file_write:
            file_write.write(file.read())
        book.image_link = image_link
        db_sess.commit()
        return redirect(f"/show_book/{book_id}")
    else:
        image = book.image_link
        if not image or not os.path.exists(image):
            image = "static/images/skins/standard-image.jpg"
        form.genre.choices = [(i.id, i.title) for i in db_sess.query(Genre).all()]
        form.title.data = book.title
        form.book_author.data = book.book_author
        form.genre.data = book.genre_id
        return render_template("edit_book_page.html", form=form, book=book, image_link=image)
        # else:
        #     file = request.files['file']
        #     with open(f"static/images/skins/{book.title}-{len(images)}.png", "wb") as file_write:
        #         file_write.write(file.read())
        #     return redirect(f"/edit_book/{book_id}")


@app.route("/delete_book/<int:book_id>", methods=["GET", "POST"])
@login_required
def delete_book(book_id):
    pass


@app.route("/add_book", methods=["GET", "POST"])
@login_required
def add_book():
    form = EditBookForm()
    return render_template("edit_book_page.html", form=form, book=book)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/main_page")


if __name__ == '__main__':
    db_session.global_init("db/books.db")
    app.run(port=8080, host='127.0.0.1')
