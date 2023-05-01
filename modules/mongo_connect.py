from pymongo import MongoClient
from bson.objectid import ObjectId
import mongoengine as me
import bcrypt

# ! With mongoengine

me.connect(alias='frota-alias', db="frota", host="mongodb://localhost:27017/")
me.connect(alias='registro-alias', db="registro", host="mongodb://localhost:27017/")


# TODO>> Car Modules
class Cars(me.DynamicDocument):
    frota = me.IntField(required=True)
    placa = me.StringField(required=True)
    meta = {
        "db_alias": "frota-alias",
        "collection": "carros"
        }


class CarTools:
    def __init__(self):
        pass

    def get_all(self):
        data = []
        for cars in Cars.objects():
            data.append({"id": cars.id, "frota": cars.frota, "placa": cars.placa})
        return data

    def get_by_id(self, id):
        for i in Cars.objects(_id=ObjectId(id)):
            car = {"id": i.id, "frota": i.frota, "placa": i.placa}
        return car

    def add_car(self, frota, placa):
        car = Cars(frota=frota, placa=placa)
        car.save()

    def update_car(self, id, frota, placa):
        Cars.objects(_id=ObjectId(id)).update(set__frota=frota, set__placa=placa)

    def delete_car(self, id):
        Cars.objects(_id=ObjectId(id)).delete()


# TODO>> Revenue Modules
class Revenues(me.DynamicDocument):
    rota = me.StringField(required=True)
    placa = me.StringField(required=True)
    motorista = me.StringField(required=True)
    monitor = me.StringField(required=True)
    meta = {
        "db_alias": "registro-alias",
        "collection": "aditivo"
        }


class RevenueTools:
    def __init__(self):
        pass

    def get_all(self):
        data = []
        for revenues in Revenues.objects():
            data.append(
                {
                    "rota": revenues.rota,
                    "placa": revenues.placa,
                    "motorista": revenues.motorista,
                    "monitor": revenues.monitor,
                }
            )
        return data


# ! With Pymongo

uri = "mongodb://localhost:27017/"

client = MongoClient(uri)

# Register DB Instance
db_register = client["registro"]
register = db_register["main"]
aditivo = db_register["aditivo"]

# Users DB Instance
db_users = client["usuarios"]
users = db_users["data"]


# Class of Register Main
class Db_Register:
    def __init__(self):
        pass

    # * Function to get MAIN data from MongoDB. Return [{}]
    def get_main_data(self):
        data = []
        for i in register.find():
            data.append(i)
        return data

    # * Function to add data to Register DB
    def add_main(
        self,
        data=str,
        ano=str,
        mes=str,
        transacao=str,
        veiculo=str,
        sg_receita=str,
        receita=str,
        descricao=str,
        nf=int,
        quantidade=int,
        valor=float,
    ):
        register.insert_one(
            {
                "data": data,
                "ano": ano,
                "mes": mes,
                "transacao": transacao,
                "veiculo": veiculo,
                "receita": receita,
                "descricao": descricao,
                "nf": nf,
                "quantidade": quantidade,
                "valor": valor,
            }
        )



# Class of Users
class Db_Users:
    def __init__(self):
        pass

    # Get Users Data
    def get_data(self):
        data = []
        for i in users.find():
            data.append(i)
        return data

    # User Register
    def new_user(self, name=str, surname=str, username=str, email=str, password=str):
        # Generate password hash
        pwd = password
        pwd_bytes = pwd.encode("utf-8")

        # Generate bcrypt salt
        salt = bcrypt.gensalt()

        # hash pwd
        hash_pwd = bcrypt.hashpw(password=pwd_bytes, salt=salt)

        # Insert User Register
        users.insert_one(
            {
                "name": name,
                "surname": surname,
                "username": username,
                "email": email,
                "password": hash_pwd,
            }
        )


# >> create part
# pwd = '3545'
# b = pwd.encode('utf-8')
# salt = bcrypt.gensalt()
# hash = bcrypt.hashpw(password=b, salt=salt)

# >> check part
# pwd2 = '3545'
# pwd_b = pwd2.encode('utf-8')
# hash_result = bcrypt.checkpw(pwd_b, hash)

# print(hash_result)