import mongoengine as me

me.connect('frota', host="mongodb://localhost:27017/")

class Frota(me.DynamicDocument):
    name = me.StringField(required=True)
    placa = me.StringField(required=True)
    meta = {'collection': 'CARRU'}

frota = Frota(name='Carro1', placa='GBX-8954')
frota.save()