from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField
from wtforms.validators import DataRequired


class FileLoad(FlaskForm):
    file_load = FileField("Добавить картинку", validators=[DataRequired()])
    submit = SubmitField('Отправить')
