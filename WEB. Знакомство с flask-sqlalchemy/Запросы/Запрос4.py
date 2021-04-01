from data import db_session
from data.users import User


filename = input()
db_session.global_init(filename)
db_sess = db_session.create_session()
for user in db_sess.query(User).filter(User.position.like("%middle%") | User.position.like("%chief%")):
    print(f"<Colonist> {user.id} {user.surname} {user.name} {user.position}")
