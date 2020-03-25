from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField


class dataForm(FlaskForm):
    water = StringField(':הכנס קריאת מונה מים ')
    electricity = StringField(':הכנס קריאת מונה חשמל ')
    apartmentA = SubmitField('דירה א')
    apartmentB = SubmitField('דירה ב')
