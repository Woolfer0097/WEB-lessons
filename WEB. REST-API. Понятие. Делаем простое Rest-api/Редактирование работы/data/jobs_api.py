from flask import Blueprint, jsonify, request

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
                [{"id": item.id, "team_leader": item.team_leader, "job": item.job,
                  "work_size": item.work_size, "collaborators": item.collaborators,
                 "is_finished": item.is_finished}
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['PUT'])
def edit_jobs(jobs_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size', 'collaborators', 'is_finished']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    id_s = [element.id for element in db_sess.query(Jobs).all()]
    if int(jobs_id) not in id_s:
        return jsonify({'error': 'ID does not exists'})
    jobs = db_sess.query(Jobs).filter(Jobs.id == jobs_id).first()
    jobs.team_leader = request.json['team_leader']
    jobs.job = request.json['job']
    jobs.work_size = request.json['work_size']
    jobs.collaborators = request.json['collaborators']
    jobs.is_finished = request.json['is_finished']
    db_sess.commit()
    return jsonify({'success': 'OK'})
