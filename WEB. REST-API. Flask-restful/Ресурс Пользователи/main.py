from flask import Flask
from data import db_session, users_resource
from flask_restful import Api

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)


def main():
    db_session.global_init("db/blogs.db")
    api.add_resource(users_resource.UsersListResource, '/api/v2/users')
    api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:user_id>')
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
