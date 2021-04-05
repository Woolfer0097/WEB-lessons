from . import db_session
from .users import User
from flask import jsonify
from flask_restful import Resource, abort
from .parser import parser


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify(
            {
                'users':
                    {
                        'surname': user.surname, 'name': user.name, 'age': user.age,
                        'position': user.position, 'speciality': user.speciality,
                        'address': user.address, 'email': user.email}
            }
        )

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify(
            {
                'users':
                    [{
                        'surname': user.surname, 'name': user.name, 'age': user.age,
                        'position': user.position, 'speciality': user.speciality,
                        'address': user.address, 'email': user.email} for user in users]
            }
        )

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email']
        )
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})
