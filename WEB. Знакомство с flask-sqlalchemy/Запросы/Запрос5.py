from data import db_session
from data.jobs import Jobs

filename = input()
db_session.global_init(filename)
db_sess = db_session.create_session()
for job in db_sess.query(Jobs).filter((Jobs.work_size < 20) & (Jobs.is_finished == 0)):
    print(f"<Job> {job.job}")
