from flask import Flask, render_template, request, redirect, url_for
from modules import mongo_connect, validations
from flask_wtf.csrf import CSRFProtect
import os

csrf = CSRFProtect()
# The secret_key is necessary to use csrf protection, so us created this.
secret_key = os.urandom(24)

# Instance of Flask App

# TODO> The Initial Function.
def create_app():
    app = Flask(__name__)
    app.secret_key = secret_key
    # To set this "csrf.init_app(app)" is necessary to add all the code inside 
    # to this function "create_app()".
    csrf.init_app(app)

    # HomePage Route
    # TODO> HOME
    @app.route("/")
    def home_page():
        form = validations.AddValidate()
        # return list with data from DataBase
        data = mongo_connect.db_management().get_data()
        return render_template("home.html", items=data, form=form)

    # POST to add item in list
    # TODO> ADD

    @app.route("/add_item", methods=["POST"])
    def add_item():
        # class "Form" receive "formdata(dict)=request.form(dict)"
        form = validations.AddValidate()
        # get input from form with name.
        # IF HTTP = POST
        if request.method == 'POST' and form.validate_on_submit():
            frota = form.frota.data  # request.form['frota'] > before
            # request.form['placa'].upper() > before
            plate = form.plate.data.upper()

            print(frota, plate)
            # append data from input in list.
            add = mongo_connect.db_management()
            add.add_to_db(frota=int(frota), placa=str(plate))

            # returning to "home_page" after to add itens in table with the list.
            return redirect(url_for("home_page"))
        else:
            print(form.errors)
            return redirect(url_for("home_page"))

    # POST to update item in list / GET to access update page.
    # TODO> UPDATE
    @app.route("/editar/<id>", methods=["GET", "POST"])
    def update(id):
        # Get specific car data.
        item_id = mongo_connect.db_management().get_by_id(str(id))

        # This is accessed from update page
        if request.method == "POST":
            # Get Form Data.
            form_frota = request.form['form_frota']
            form_plate = request.form['form_placa'].upper()

            # get old data.
            old_frota = item_id['frota']
            old_plate = item_id['placa']

            # get new data
            new_frota = int(form_frota)
            new_plate = form_plate

            # Set update in DB
            mongo_connect.db_management().update_data(
                old_frota, new_frota, old_plate, new_plate)

            # Redirect to page
            return redirect(url_for("home_page"))

        # This is accessed from home page
        elif request.method == "GET":
            # Return to update form
            return render_template("update.html", item=item_id)

    # TODO> DELETE

    @app.route("/deletar/<id>", methods=["GET", "POST"])
    def delete(id):
        mongo_connect.db_management().delete_data(id)
        return redirect(url_for('home_page'))

    # Main execute
    if __name__ == "__main__":
        app.run(debug=True)


create_app()
