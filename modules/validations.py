from wtforms import StringField, validators, SubmitField, DateField, SelectField
from flask_wtf import FlaskForm
from modules import mongo_connect


""" Form as a parameter indicating this class "add_validate"
is a subclass of "Form", so 'add_validate' inherits (herda)
the attributes for class 'Form'"""


db_cars = mongo_connect.CarTools()
db_receitas = mongo_connect.RegisterTools()
db_revenue = mongo_connect.RevenueTools()
db_users = mongo_connect.Db_Users()


# TODO>> CUSTOM VALIDATORS


def frota_exist(form, field):
    frota = db_cars.get_all()
    for i in frota:
        if int(field.data) == int(i["frota"]):
            raise validators.ValidationError("* Veículo já cadastrado")


# ? Users Data Validations
def email_exist(form, field):
    users = db_users.get_data()
    for user in users:
        if str(user["email"]) == str(field.data):
            raise validators.ValidationError("* Email já está cadastrado")


def username_exist(form, field):
    users = db_users.get_data()
    for user in users:
        if str(user["username"]) == str(field.data):
            raise validators.ValidationError("* Nome de usúario já cadastrado")


# TODO>> === FORMS ===


# TODO>> Add Validations
class AddCars(FlaskForm):
    frota = StringField(
        "Frota",
        [
            validators.DataRequired(message="Insira o número da frota"),
            validators.length(min=2, max=3),
            frota_exist,
        ],
    )
    plate = StringField(
        "Placa", [validators.DataRequired(), validators.length(min=7, max=8)]
    )
    add_btn = SubmitField("Adicionar")
    edit_btn = SubmitField("Editar")
    delete_btn = SubmitField("Deletar")


# TODO>> Add Register
class AddRegister(FlaskForm):
    # Data Form
    data = DateField(
        [validators.DataRequired(message="Insira a Data")], format="%Y-%m-%d"
    )

    # Year Form
    year = StringField("Ano", [validators.DataRequired(message="Insira o ano")])

    # Mounth Form
    mounth = SelectField(
        [validators.DataRequired()],
        choices=[
            ("janeiro", "Janeiro"),
            ("fevereiro", "Fevereiro"),
            ("março", "Março"),
            ("abril", "Abril"),
            ("maio", "Maio"),
            ("junho", "Junho"),
            ("julho", "Julho"),
            ("agosto", "Agosto"),
            ("setembro", "Setembro"),
            ("outubro", "Outubro"),
            ("novembro", "Novembro"),
            ("dezembro", "Dezembro"),
        ],
    )

    # Type Form
    transaction = SelectField(
        [validators.DataRequired()],
        choices=[("credito", "Credito"), ("debito", "Debito")],
    )

    # Vehicle Form
    cars = SelectField(
        [validators.DataRequired()],
        choices=[i["placa"] for i in db_cars.get_all()],
        id="veiculos",
    )

    # Sg Receitas
    revenues = SelectField(
        [validators.DataRequired()],
        choices=[i["rota"] for i in db_revenue.get_all()],
        id="receitas",
    )

    add_btn = SubmitField("Adicionar")


# TODO>> Add Revenue
class AddRevenue(FlaskForm):
    rota = StringField("Rota", [validators.DataRequired()])
    placa = StringField("Placa", [validators.DataRequired()])
    motorista = StringField("Motorista", [validators.DataRequired()])
    monitor = StringField("Monitor", [validators.DataRequired()])
    add_btn = SubmitField("Adicionar")


# TODO>> Add Users
class AddUsers(FlaskForm):
    # UserName
    name = StringField(
        "Nome",
        [validators.DataRequired()],
        render_kw={
            "class": "form-control",
            "type": "text",
            "placeholder": "Insira seu nome",
        },
    )
    surname = StringField(
        "Sobrenome",
        [validators.DataRequired()],
        render_kw={
            "class": "form-control",
            "type": "text",
            "placeholder": "Insira seu sobrenome",
        },
    )
    username = StringField(
        "Username",
        [validators.DataRequired(), username_exist],
        render_kw={
            "class": "form-control",
            "type": "text",
            "placeholder": "Insira seu nome de usúario",
        },
    )
    email = StringField(
        "Email",
        [
            validators.DataRequired(),
            validators.Email(message="* Email inválido"),
            email_exist,
        ],
        render_kw={
            "class": "form-control",
            "type": "email",
            "placeholder": "Insira seu email",
        },
    )
    password = StringField(
        "Password",
        [
            validators.DataRequired(),
            validators.EqualTo("repassword", message="* As senhas precisam ser iguais"),
        ],
        render_kw={
            "class": "form-control",
            "type": "password",
            "placeholder": "Insira sua senha",
        },
    )
    repassword = StringField(
        "Repassword",
        [validators.DataRequired(message="Insira a senha")],
        render_kw={
            "class": "form-control",
            "type": "password",
            "placeholder": "Insira sua senha",
        },
    )
    register_btn = SubmitField("Cadastrar")
