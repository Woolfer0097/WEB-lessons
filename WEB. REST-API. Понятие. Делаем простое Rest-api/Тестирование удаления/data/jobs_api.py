from flask import Blueprint, jsonify

from . import db_session
from .jobs import Jobs

blueprint = Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs', methods=['GET'])
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [{"id": item.id, "team_leader": item.team_leader,
                  "work_size": item.work_size, "collaborators": item.collaborators,
                 "is_finished": item.is_finished}
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['DELETE'])
def delete_jobs(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)
    if not jobs:
        return jsonify({'error': 'Id does not exist'})
    db_sess.delete(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})
