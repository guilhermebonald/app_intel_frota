from flask import Flask, render_template, request, redirect, url_for
from modules import mongo_connect

# Instance of Flask App
app = Flask(__name__)


# HomePage Route
@app.route("/")
def home_page():
    # return list with data from DataBase
    data = mongo_connect.db_management().get_data()
    return render_template("home.html", items=data)


# POST to add item in list
@app.route("/add_item", methods=["POST"])
def add():
    # get input from form with name.
    frota = request.form['frota']
    placa = request.form['placa'].upper()
    # append data from input in list.
    add = mongo_connect.db_management()
    add.add_to_db(frota=int(frota), placa=str(placa))
    # returning to "home_page" after to add itens in table with the list.
    return redirect(url_for("home_page"))


# POST to edit item in list
@app.route("/edit/<id>", methods=["GET", "POST"])
def update(_id):
    item = _id
    pass

# Main execute
if __name__ == "__main__":
    app.run(debug=True)
