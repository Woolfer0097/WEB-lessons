from data import db_session
from data.users import User
from data.jobs import Jobs

filename = input()
db_session.global_init(filename)
db_sess = db_session.create_session()
teams = []
for job in db_sess.query(Jobs).all():
    teams.append(len(job.collaborators.split(", ")))
for job in db_sess.query(Jobs):
    if len(job.collaborators.split(", ")) == max(teams):
        for user in db_sess.query(User).filter(User.id == job.team_leader):
            print(user.surname, user.name)
