from flask import Flask
from data import db_session, jobs_resource
from flask_restful import Api

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)


def main():
    db_session.global_init("db/blogs.db")
    api.add_resource(jobs_resource.JobsListResource, '/api/v2/jobs')
    api.add_resource(jobs_resource.JobsResource, '/api/v2/jobs/<int:job_id>')
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
