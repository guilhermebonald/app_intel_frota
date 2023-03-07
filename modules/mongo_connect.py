from pymongo import MongoClient

uri = "mongodb://localhost:27017/"

client = MongoClient(uri)
db = client["frota"]
car = db["carros"]


class db_management:
    def __init__(self):
        pass

    def get_data(self):
        cars = []
        for i in car.find():
            cars.append(i)
        return cars

    def add_to_db(self, frota=int, placa=str):
        car.insert_one(
            {"frota": frota, "placa": placa}
        )