# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import InputRequired

class UploadForm(FlaskForm):
    photo = FileField('photo',validators=[FileRequired(),FileAllowed(['jpg', 'png', 'jpeg'], 'Illegal file detected.')])
    description = TextAreaField('description', validators=[InputRequired()])