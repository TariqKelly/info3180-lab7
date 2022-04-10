# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename



class UploadForm(FlaskForm):
    photo = FileField('Image', validators=[
        FileRequired(), 
        FileAllowed(['jpg','png'], 'Images Only!')
        ])
    description = TextAreaField('Description', validators=[DataRequired()])