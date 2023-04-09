from pymongo import MongoClient
from bson.objectid import ObjectId

uri = "mongodb://localhost:27017/"

client = MongoClient(uri)

# Car DB Instance
db_car = client["frota"]
car = db_car["carros"]

# Register DB Instance
db_register = client["registro"]
register = db_register["main"]
aditivo = db_register["aditivo"]

# Class of cars


class Db_Cars:
    def __init__(self):
        pass

    # * Function to get data fro MongoDB. Return [{}]
    def get_data(self):
        data = []
        for i in car.find():
            data.append(i)
        return data

    # * Function to get unique but complete data by ID. Return {}
    def get_by_id(self, id=str):
        return car.find_one(
            {"_id": ObjectId(id)}
        )

    # * Function to add data in DB.
    def add_to_db(self, frota=int, placa=str):
        car.insert_one(
            {"frota": frota, "placa": placa}
        )

    # * Function to update data in DB.
    def update_data(self, old_frota=int, new_frota=int, old_plate=str, new_plate=str):
        # Frota Value Update
        car.update_one(
            {"frota": old_frota},
            {"$set": {"frota": new_frota}}
        )

        # Placa Value Update
        car.update_one(
            {"placa": old_plate},
            {"$set": {"placa": new_plate}},
        )

    # * Function to delete data from DB.
    def delete_data(self, id=str):
        car.delete_one(
            {"_id": ObjectId(id)}
        )


# Class of Register
class Db_Register:
    def __init__(self):
        pass

    # * Function to get data fro MongoDB. Return [{}]
    def get_data(self):
        data = []
        for i in register.find():
            data.append(i)
        return data

    # * Function to add data to Register DB
    def add_to_db(self, data=str, ano=str, mes=str, transacao=str, veiculo=str, sg_receita=str, receita=str, descricao=str, nf=int, quantidade=int, valor=float):
        register.insert_one(
            {'data': data, 'ano': ano, 'mes': mes, 'transacao': transacao, 'veiculo': veiculo, 'sug_receita': sg_receita,
                'receita': receita, 'descricao': descricao, 'nf': nf, 'quantidade': quantidade, 'valor': valor}
        )


# Db_Register().add_to_db('data', 'ano', 'mes', 'transacao', 'veiculo',
#                       'sug_receita', 'receita', 'descricao', 2345, 2, 123.43)
