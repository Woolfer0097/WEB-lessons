from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    team_leader = IntegerField('Лидер команды', validators=[DataRequired()])
    job = StringField('Работа', validators=[DataRequired()])
    work_size = IntegerField('Длина работы', validators=[DataRequired()])
    collaborators = StringField('Члены команды', validators=[DataRequired()])
    is_finished = BooleanField('Работа завершена')
    submit = SubmitField('Добавить/Изменить')
