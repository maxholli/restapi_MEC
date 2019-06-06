from rest_api_demo.database import db
from rest_api_demo.database.models import UE, Subscription, Server

## create UE
def create_ue(data):
    ue_name = data.get('name')
    ip = data.get('ue_ip')
    ue = UE(ue_name, ip)
    db.session.add(ue)
    db.session.commit()

## create Subscription
def create_sub(data):
    sub_name = data.get('name')
    port = data.get('port')
    sub = Subscription(sub_name, port)
    db.session.add(sub)
    db.session.commit()

## create Server
def create_ser(data):
    ip = data.get('ser_ip')
    ser = Server(ip)
    db.session.add(ser)
    db.session.commit()
    
## add link between UE and subscription
def update_ue_sub(ue_ip, data): 
    name = data.get('name')
    ue = UE.query.filter(UE.ue_ip == ue_ip).one()
    sub = Subscription.query.filter(Subscription.name == name).one()
    ue.ue_sub.append(sub)
    db.session.add(ue)
    db.session.commit()

## add link between subscription and server
def update_sub_server(name, data): 
    ip = data.get('ser_ip')
    ser = Server.query.filter(Server.ser_ip == ip).one()
    sub = Subscription.query.filter(Subscription.name == name).one()
    sub.sub_server.append(ser)
    db.session.add(sub)
    db.session.commit()
    
def delete_ue(ue_ip):
    ue = UE.query.filter(UE.ue_ip == ue_ip).one()
    db.session.delete(ue)
    db.session.commit()

def delete_sub(sub_name):
    sub = Subscription.query.filter(Subscription.name == sub_name).one()
    db.session.delete(sub)
    db.session.commit()

def delete_ser(ser_ip):
    ser = Server.query.filter(Server.ser_ip == ser_ip).one()
    db.session.delete(ser)
    db.session.commit()

def delete_all_ues(ues):
    for ue in ues:
        db.session.delete(ue)
        db.session.commit()
