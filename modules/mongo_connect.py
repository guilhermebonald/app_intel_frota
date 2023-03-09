from pymongo import MongoClient

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
        #    parse = {}
        #    parse["id"] = str(i["_id"])
        #    parse["frota"] = int(i["frota"])
        #    parse["placa"] = str(i["placa"])
        #    data.append(parse)
            data.append(i)
        return data

    def add_to_db(self, frota=int, placa=str):
        car.insert_one(
            {"frota": frota, "placa": placa}
        )

    def edit_data(self, _id=str):
        car.find(
            {"_id": _id}
        )

    def delete_data(self, id):
        car.delete_one(
            {"_id": id}
        )
