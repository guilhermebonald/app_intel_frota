from flask import Flask, render_template, request, redirect, url_for
from modules import mongo_connect, validations
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
import os


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
        data = mongo_connect.Db_Register().get_main_data()
        return render_template("pages/home_register.html", items=data, form=form)

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
        form = validations.AddValidate()
        # return list with data from DataBase
        data = mongo_connect.Db_Cars().get_data()
        return render_template("pages/cars.html", items=data, form=form)

    # POST to add item in list
    # * ADD Car Function
    @app.route("/add_car", methods=["POST"])
    def add_car():
        # class "Form" receive "formdata(dict)=request.form(dict)"
        form = validations.AddValidate()
        # get input from form with name.
        # IF HTTP = POST
        if request.method == "POST" and form.validate_on_submit():
            frota = form.frota.data
            plate = form.plate.data.upper()
            if len(plate) == 7:
                plate = plate[:3] + "-" + plate[3:]

            # append data from input in list.
            add = mongo_connect.Db_Cars()
            add.add_to_db(frota=int(frota), placa=str(plate))

            # returning to "home_page" after to add itens in table with the list.
            return redirect(url_for("cars"))
        else:
            return redirect(url_for("cars"))

    # POST to update item in list / GET to access update page.
    # * UPDATE Car Function
    @app.route("/edit_car/<id>", methods=["GET", "POST"])
    def update_car(id):
        # Get specific car data.
        item_by_id = mongo_connect.Db_Cars().get_by_id(str(id))
        form = validations.AddValidate()

        # 2° - This is accessed from update page
        if request.method == "POST":
            # Get Form Data.
            form_frota = form.frota.data
            form_plate = form.plate.data.upper()

            # get old data.
            old_frota = item_by_id["frota"]
            old_plate = item_by_id["placa"]

            # get new data
            new_frota = int(form_frota)
            new_plate = form_plate

            # Set update in DB
            mongo_connect.Db_Cars().update_data(
                old_frota, new_frota, old_plate, new_plate
            )

            # Redirect to page
            return redirect(url_for("cars"))

        # 1° - This is accessed from home page
        elif request.method == "GET":
            # Return to update form
            return render_template(
                "elements_pages/update_car.html", form=form, item=item_by_id
            )

    # * DELETE Car Function
    @app.route("/delete_car/<id>", methods=["GET", "POST"])
    def delete_car(id):
        mongo_connect.Db_Cars().delete_data(id)
        return redirect(url_for("cars"))

    # ! ==== REVENUE RULES PAGE ====
    @app.route("/receitas")
    def revenues():
        data = mongo_connect.Db_Revenue().get_revenue_data()
        form = validations.AddRevenue()
        return render_template("pages/revenues.html", items=data, form=form)

    # ! ==== AUTH RULES PAGE ====
    @app.route("/user_register", methods=["GET", "POST"])
    def user_register():
        form = validations.AddUsers()

        if request.method == "POST" and form.validate_on_submit():
            name = form.name.data
            surname = form.surname.data
            username = form.username.data
            email = form.email.data
            password = form.password.data

            mongo_connect.Db_Users().new_user(
                name=str(name),
                surname=str(surname),
                username=str(username),
                email=str(email),
                password=str(password),
            )

            return redirect(url_for("home_page"))

        return render_template("pages/user_register.html", form=form)

    # ! MAIN EXECUTE
    if __name__ == "__main__":
        app.run(debug=True)


create_app()