from wtforms import StringField, validators, SubmitField, DateField, SelectField
from flask_wtf import FlaskForm
from modules import mongo_connect


""" Form as a parameter indicating this class "add_validate"
is a subclass of "Form", so 'add_validate' inherits (herda)
the attributes for class 'Form'"""


db_cars = mongo_connect.Db_Cars()


# Custom Validators
def frota_exist(form, field):
    frota = db_cars.get_data()
    for i in frota:
        if int(field.data) == int(i["frota"]):
            raise validators.ValidationError('Veículo já cadastrado.')


# Add Validations
class AddValidate(FlaskForm):
    frota = StringField(
        "Frota", [validators.DataRequired(message="Insira o número da frota"), validators.length(min=2, max=3), frota_exist])
    plate = StringField(
        "Placa", [validators.DataRequired(), validators.length(min=7, max=8)])
    add_btn = SubmitField('Adicionar')
    edit_btn = SubmitField('Editar')
    delete_btn = SubmitField('Deletar')


# Add Register
class AddRegister(FlaskForm):
    # Data Form
    data = DateField([validators.DataRequired(
        message="Insira a Data")], format='%Y-%m-%d')
    
    # Year Form
    ano = StringField('Ano', [validators.DataRequired(message="Insira o ano")], )

    # Mounth Form
    mes = SelectField([validators.DataRequired()],
                      choices=[('janeiro', 'Janeiro'), ('fevereiro', 'Fevereiro'), ('março', 'Março'), ('abril', 'Abril'), ('maio', 'Maio'), ('junho', 'Junho'),
                               ('julho', 'Julho'), ('agosto', 'Agosto'), ('setembro', 'Setembro'), ('outubro', 'Outubro'), ('novembro', 'Novembro'), ('dezembro', 'Dezembro')])
    
    # Type Form 
    transacao = SelectField([validators.DataRequired()],
                            choices=[('credito', 'Credito'), ('debito', 'Debito')])
    
    # Vehicle Form
    veiculos = SelectField(
        [validators.DataRequired()],
        choices=[
            i['placa'] for i in db_cars.get_data()
        ]
    )
    add_btn = SubmitField('Adicionar')
