from data import db_session
from data.users import User
from data.jobs import Jobs


filename = input()
db_session.global_init(filename)
db_sess = db_session.create_session()
teams = []
for job in db_sess.query(Jobs).all():
    teams.append(len(job.collaborators.split(", ")))
result_data = set()
for job in db_sess.query(Jobs):
    if len(job.collaborators.split(", ")) == max(teams):
        for user in db_sess.query(User).filter(User.id == job.team_leader):
            result_data.add(f"{user.name} {user.surname}")
print("\n".join(result_data))
