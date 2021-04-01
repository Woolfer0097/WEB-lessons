from data import db_session
from data.jobs import Jobs
from data.department import Department
from data.users import User

# .filter(Department.id == 1)
filename = input()
db_session.global_init(filename)
db_sess = db_session.create_session()
for member in db_sess.query(Department):
    print(member)
# for user in db_sess.query(User).filter((User.age < 21) & (User.address == "module_1")):
#     user.address = "module_3"
#     db_sess.commit()
