import mongoengine as me

me.connect(db='frota', host="mongodb://localhost:27017/")

class Cars(me.DynamicDocument):
    frota = me.IntField(required=True)
    placa = me.StringField(required=True)
    meta = {'collection': 'carros'}


class DbTools():
    def __init__(self):
        pass

    def add_car(self, frota, placa):
        car = Cars(frota=frota, placa=placa)
        car.save()

    def update_car(self, s_frota, u_frota, u_placa):
        Cars.objects(frota=s_frota).update(set__frota=u_frota, set__placa=u_placa)

    
    def delete_car(self, frota):
        car = Cars.objects(frota=frota).delete()