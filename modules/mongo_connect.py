from pymongo import MongoClient
from bson.objectid import ObjectId

uri = "mongodb://localhost:27017/"

client = MongoClient(uri)
db = client["frota"]
car = db["carros"]


class db_management:
    def __init__(self):
        pass

    def get_data(self):
        data = []
        for i in car.find():
            data.append(i)
        return data

    def get_by_id(self, id=str):
        return car.find_one(
            {"_id": ObjectId(id)}
        )

    def add_to_db(self, frota=int, placa=str):
        car.insert_one(
            {"frota": frota, "placa": placa}
        )

    def update_data(self, frota=int, placa=str):
        # Frota Value Update
        car.update_one(
            {"frota": 65},
            {"$set": {"frota": 76}}
        )

        # Placa Value Update
        car.update_one(
            {"placa": "GBB-6423"},
            {"$set": {"placa": "YGH-8324"}},
        )

    def delete_data(self, id=str):
        car.delete_one(
            {"_id": ObjectId(id)}
        )


db_management().update_data()
