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

class Db_Register:
    def __init__(self):
        pass
    
    # * Function to get data fro MongoDB. Return [{}]
    def get_data():
        data = []
        for i in register.find():
            data.append(i)
        return data
        