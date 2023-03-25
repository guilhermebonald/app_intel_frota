from wtforms import StringField, PasswordField, validators, SubmitField
from flask_wtf import FlaskForm


""" Form as a parameter indicating this class "add_validate"
is a subclass of "Form", so 'add_validate' inherits (herda)
the attributes for class 'Form'"""


class AddValidate(FlaskForm):
    frota = StringField("Frota", [validators.DataRequired()])
    plate = StringField(
        "Placa", [validators.DataRequired()])
    btn = SubmitField('Adicionar')
