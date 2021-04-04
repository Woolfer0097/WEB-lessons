from flask import Blueprint, jsonify, request

from . import db_session
from .users import User

blueprint = Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/users', methods=['GET'])
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            'users':
                [{'surname': user.surname, 'name': user.name, 'age': user.age, 'position': user.position,
                  'speciality': user.speciality, 'address': user.address, 'email': user.email}
                 for user in users]
        }
    )


@blueprint.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    return jsonify(
        {
            'users': {'surname': user.surname, 'city_from': user.city_from,
                      'name': user.name, 'age': user.age,
                      'speciality': user.speciality, 'address': user.address,
                      'email': user.email, 'position': user.position}
        }
    )


@blueprint.route('/api/users/<user_id>', methods=['POST'])
def create_user(user_id):
    if not user_id.isdigit():
        return jsonify({'error': 'ID must be integer'})
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['surname', 'city_from', 'name', 'age', 'position', 'speciality', 'address', 'email']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    id_s = [element.id for element in db_sess.query(User.id).all()]
    if int(user_id) in id_s:
        return jsonify({'error': 'Id already exists'})
    user = User(
        id=user_id,
        surname=request.json['surname'],
        city_from=request.json['city_from'],
        name=request.json['name'],
        age=request.json['age'],
        position=request.json['position'],
        speciality=request.json['speciality'],
        address=request.json['address'],
        email=request.json['email']
    )
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'ID does not exist'})
    db_sess.delete(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:user_id>', methods=['PUT'])
def edit_users(user_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['surname', 'city_from', 'name', 'age', 'position', 'speciality', 'address', 'email']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    id_s = [element.id for element in db_sess.query(User).all()]
    if int(user_id) not in id_s:
        return jsonify({'error': 'ID does not exists'})
    user = db_sess.query(User).filter(User.id == user_id).first()
    user.surname = request.json['surname']
    user.city_from = request.json['city_from']
    user.name = request.json['name']
    user.age = request.json['age']
    user.position = request.json['position']
    user.speciality = request.json['speciality']
    user.address = request.json['address']
    user.email = request.json['email']
    db_sess.commit()
    return jsonify({'success': 'OK'})
