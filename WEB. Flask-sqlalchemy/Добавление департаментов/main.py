from flask import Flask, render_template, redirect, abort, request
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.department import Department
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from forms.login import LoginForm
from forms.register import RegisterForm
from forms.job import JobForm
from forms.department import DepartmentForm

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
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            email=form.email.data,
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect("/login")
    return render_template('register.html', title='Регистрация', form=form)


@app.route("/")
def index():
    return render_template("main_page.html", title="Главная страница")


@app.route("/<table_type>")
def main_page(table_type):
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        if table_type == "job":
            jobs = db_sess.query(Jobs).filter(Jobs.team_leader == current_user.id).all()
            data = [{'id': job.id, 'team_leader': job.team_leader, 'job': job.job, 'work_size': job.work_size,
                    'collaborators': job.collaborators, 'is_finished': job.is_finished} for job in jobs]
            return render_template("main_page.html", title="Главная страница", data=data, job_flag=True)
        else:
            departments = db_sess.query(Department).filter(Department.chief == current_user.id).all()
            data = [{'id': department.id, 'title': department.title, 'chief': department.chief,
                     'members': department.members, 'email': department.email}
                    for department in departments]
            return render_template("main_page.html", title="Главная страница", data=data, department_flag=True)


@app.route("/add_job", methods=["GET", "POST"])
def add_job():
    form = JobForm()
    form.team_leader.data = current_user.id
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = Jobs()
        jobs.team_leader = form.team_leader.data
        jobs.job = form.job.data
        jobs.work_size = form.work_size.data
        jobs.collaborators = form.collaborators.data
        jobs.is_finished = form.is_finished.data
        user = db_sess.query(User).filter(User.id == jobs.team_leader).first()
        user.jobs.append(jobs)
        db_sess.merge(user)
        db_sess.commit()
        return redirect("/job")
    return render_template("job.html", title="Добавление работы", form=form)


@app.route('/edit_job/<int:job_id>', methods=['GET', 'POST'])
@login_required
def edit_jobs(job_id):
    form = JobForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == job_id,
                                          (Jobs.team_leader == current_user.id)
                                          | (current_user.id == 1)).first()
        if jobs:
            form.team_leader.data = current_user.id
            form.job.data = jobs.job
            form.work_size.data = jobs.work_size
            form.collaborators.data = jobs.collaborators
            form.is_finished.data = jobs.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == job_id,
                                          (Jobs.team_leader == current_user.id)
                                          | (current_user.id == 1)).first()
        if jobs:
            jobs.team_leader = form.team_leader.data
            jobs.job = form.job.data
            jobs.work_size = form.work_size.data
            jobs.collaborators = form.collaborators.data
            jobs.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/job')
        else:
            abort(404)
    return render_template('job.html',
                           title='Редактирование новости',
                           form=form
                           )


@app.route('/job_delete/<int:job_id>', methods=['GET', 'POST'])
@login_required
def job_delete(job_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == job_id,
                                      (Jobs.team_leader == current_user.id)
                                      | (current_user.id == 1)).first()
    if jobs:
        db_sess.delete(jobs)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/job')


@app.route("/add_department", methods=["GET", "POST"])
@login_required
def add_department():
    form = DepartmentForm()
    form.chief.data = current_user.id
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        department = Department()
        department.title = form.title.data
        department.chief = form.chief.data
        department.members = form.members.data
        department.email = form.email.data
        user = db_sess.query(User).filter(User.id == department.chief).first()
        user.department.append(department)
        db_sess.merge(user)
        db_sess.commit()
        return redirect("/department")
    return render_template("department.html", title="Добавление департамента", form=form)


@app.route('/edit_department/<int:department_id>', methods=['GET', 'POST'])
@login_required
def edit_department(department_id):
    form = DepartmentForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        department = db_sess.query(Department).filter(Department.id == department_id,
                                                      (Department.chief == current_user.id)
                                                      | (current_user.id == 1)).first()
        if department:
            form.title.data = department.title
            form.chief.data = department.chief
            form.members.data = department.members
            form.email.data = department.email
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        department = db_sess.query(Department).filter(Department.id == department_id,
                                                      (Department.chief == current_user.id)
                                                      | (current_user.id == 1)).first()
        if department:
            department.title = form.title.data
            department.chief = form.chief.data
            department.members = form.members.data
            department.email = form.email.data
            db_sess.commit()
            return redirect('/department')
        else:
            abort(404)
    return render_template('department.html',
                           title='Редактирование департамента',
                           form=form
                           )


@app.route('/department_delete/<int:department_id>', methods=['GET', 'POST'])
@login_required
def department_delete(department_id):
    db_sess = db_session.create_session()
    departments = db_sess.query(Department).filter(Department.id == department_id,
                                                   (Department.chief == current_user.id)
                                                   | (current_user.id == 1)).first()
    if departments:
        db_sess.delete(departments)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/department')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')
