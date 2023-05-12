from flask import Flask, render_template, request, redirect, url_for, jsonify
from modules import mongo_connect, validations
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from flask_login import LoginManager
import os
from bson import json_util


# * The Initial Function.


def create_app():
    csrf = CSRFProtect()

    # Load SECRET_KEY to .env file.
    load_dotenv()

    # Start
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY")

    """
    To set this "csrf.init_app(app)" is necessary to add all the code inside
    to this function "create_app()".
    """
    csrf.init_app(app)

    # ! ==== REGISTER RULES PAGE ====
    @app.route("/")
    def home_page():
        form = validations.AddRegister()
        # return list with data from DataBase
        data = mongo_connect.RegisterTools().get_all()
        return render_template(
            "pages/register/home_register.html", items=data, form=form
        )

    # * ADD Register Function
    @app.route("/add_register", methods=["POST"])
    def add_register():
        form = validations.AddRegister()

        if request.method == "POST" and form.validate_on_submit():
            # Get Forms
            data = form.data.data.strftime("%d/%m/%Y")
            ano = form.ano.data
            mes = form.mes.data.upper()
            transacao = form.transacao.data.upper()
            veiculo = form.cars.data
            receita = form.receitas.data

            # Access function and add to DB
            add = mongo_connect.Db_Register()
            add.add_main(
                data=str(data),
                ano=str(ano),
                mes=str(mes),
                transacao=str(transacao),
                veiculo=str(veiculo),
                receita=receita,
                descricao="",
                nf=0,
                quantidade=0,
                valor=0.0,
            )
            # print(type(transacao), transacao)

            # Redirect
            return redirect(url_for("home_page"))
        else:
            return redirect(url_for("home_page"))

    # ! ==== VEHICLE RULES PAGE ====
    @app.route("/veiculos")
    def cars():
        form = validations.AddCars()
        # return list with data from DataBase
        data = mongo_connect.CarTools().get_all()
        return render_template("pages/cars/cars.html", items=data, form=form)

    # POST to add item in list
    # * ADD Car Function
    @app.route("/add_car", methods=["POST"])
    def add_car():
        # class "Form" receive "formdata(dict)=request.form(dict)"
        form = validations.AddCars()
        # get input from form with name.
        # IF HTTP = POST
        if request.method == "POST" and form.validate_on_submit():
            frota = form.frota.data
            plate = form.plate.data.upper()
            if len(plate) == 7:
                plate = plate[:3] + "-" + plate[3:]

            # append data from input in list.
            mongo_connect.CarTools().add_car(frota=frota, placa=plate)
            cars = mongo_connect.CarTools().get_all()

            # returning to "home_page" after to add itens in table with the list.
            return json_util.dumps(cars)
        else:
            return jsonify({"status": "Failed"})

    # POST to update item in list / GET to access update page.
    # * UPDATE Car Function
    @app.route("/edit_car/<id>", methods=["GET", "POST"])
    def update_car(id):
        item_by_id = mongo_connect.CarTools().get_by_id(id)
        form = validations.AddCars()

        # 2° - This is accessed from update page
        if request.method == "POST":
            # Get Form Data.
            form_frota = form.frota.data
            form_plate = form.plate.data.upper()
            if len(form_plate) == 7:
                form_plate = form_plate[:3] + "-" + form_plate[3:]

            # get id
            u_id = item_by_id["id"]

            # Set update in DB
            mongo_connect.CarTools().update_car(
                id=u_id, frota=int(form_frota), placa=form_plate
            )

            # Redirect to page
            return redirect(url_for("cars"))

        # 1° - This is accessed from home page
        elif request.method == "GET":
            # Return to update form
            return render_template(
                "pages/cars/update_car.html", form=form, item=item_by_id
            )

    # * DELETE Car Function
    @app.route("/delete_car/<id>", methods=["GET", "POST"])
    def delete_car(id):
        print(id)
        mongo_connect.CarTools().delete_car(id)
        return redirect(url_for("cars"))

    # ! ==== REVENUE RULES PAGE ====
    @app.route("/receitas")
    def revenues():
        data = mongo_connect.RevenueTools().get_all()
        form = validations.AddRevenue()
        return render_template("pages/revenues/revenues.html", items=data, form=form)

    # ! ==== AUTH RULES PAGE ====
    @app.route("/user_register", methods=["GET", "POST"])
    def user_register():
        form = validations.AddUsers()

        if request.method == "POST" and form.validate_on_submit():
            name = form.name.data
            surname = form.surname.data
            username = form.username.data
            email = form.email.datadas
            password = form.password.data

            mongo_connect.Db_Users().new_user(
                name=str(name),
                surname=str(surname),
                username=str(username),
                email=str(email),
                password=str(password),
            )

            return redirect(url_for("home_page"))

        return render_template("pages/user/user_register.html", form=form)

    # ! MAIN EXECUTE
    if __name__ == "__main__":
        app.run(debug=True)


create_app()
