from wtforms import Form, StringField, PasswordField, validators, SubmitField


class to_validate:
    def add_validate(Form):
        frota = StringField("Frota", [validators.DataRequired()])
        plate = StringField(
            "Placa", [validators.DataRequired(), validators.Length(max=7, min=6)])

    def frota_validate(Form):
        pass
