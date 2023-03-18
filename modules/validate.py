from wtforms import Form, StringField, PasswordField, validators, SubmitField

""" Form as a parameter indicating this class "add_validate"
is a subclass of "Form", so 'add_validate' inherits (herda)
the attributes for class 'Form'"""

class add_validate(Form): #Form(formdata=request.form[is dict])
    frota = StringField("Frota", [validators.DataRequired()])
    plate = StringField(
        "Placa", [validators.DataRequired(), validators.Length(max=7, min=6)])
