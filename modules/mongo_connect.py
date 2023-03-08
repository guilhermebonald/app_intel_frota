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
           parse = {}
           parse["id"] = str(i["_id"])
           parse["frota"] = int(i["frota"])
           parse["placa"] = str(i["placa"])
           data.append(parse)
        return data

    def add_to_db(self, frota=int, placa=str):
        car.insert_one(
            {"frota": frota, "placa": placa}
        )

    def edit_data(self, frota=int):
        car.update_many(
            {"frota": frota},
            {'$set': {"frota": 58}}
        )


for i in db_management().get_data():
    print(i)