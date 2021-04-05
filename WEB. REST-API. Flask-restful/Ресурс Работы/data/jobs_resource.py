from . import db_session
from .jobs import Jobs
from flask import jsonify
from flask_restful import Resource, abort
from .parser import parser


def abort_if_user_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"Job {job_id} not found")


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_user_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        return jsonify(
            {
                'jobs':
                    {
                        'team_leader': job.team_leader, 'job': job.job, 'work_size': job.work_size,
                        'collaborators': job.collaborators, 'is_finished': job.is_finished
                    }
            }
        )

    def delete(self, job_id):
        abort_if_user_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})

    def put(self, job_id):
        abort_if_user_not_found(job_id)
        args = parser.parse_args()
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        job.team_leader = args['team_leader']
        job.job = args['job']
        job.work_size = args['work_size']
        job.collaborators = args['collaborators']
        job.is_finished = args['is_finished']
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify(
            {
                'jobs':
                    [{
                        'team_leader': job.team_leader, 'job': job.job, 'work_size': job.work_size,
                        'collaborators': job.collaborators, 'is_finished': job.is_finished}
                        for job in jobs]
            }
        )

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        job = Jobs(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            is_finished=args['is_finished']
        )
        session.add(job)
        session.commit()
        return jsonify({'success': 'OK'})
