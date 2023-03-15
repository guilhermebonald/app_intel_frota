from wtforms import Form, BooleanField, StringField, PasswordField, validators

class to_validate:
    def __init__(self):
        pass

    def plate_validate(Form):
        plate = StringField("Placa", [validators.data_required()])
        

    def frota_validate(Form):
        pass
