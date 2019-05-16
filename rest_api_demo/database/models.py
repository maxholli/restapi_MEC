# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

from datetime import datetime

from rest_api_demo.database import db


UE_SUB = db.Table('ue_sub',
                  db.Column('ue_ip_br', db.String(15), db.ForeignKey('ue.ue_ip'), primary_key=True),
                  db.Column('sub_name_br', db.String(50), db.ForeignKey('subscription.name'), primary_key=True)
)

SUB_SERVER = db.Table('sub_server',
                  db.Column('ser_ip_tr', db.String(15), db.ForeignKey('server.ser_ip'), primary_key=True),
                  db.Column('sub_name_tr', db.String(50), db.ForeignKey('subscription.name'), primary_key=True)
)
    
class UE(db.Model):
    __tablename__ = 'ue'
    name = db.Column(db.String(50), nullable=False)
    ue_ip = db.Column(db.String(15), unique=True, nullable=False, primary_key=True)
    ue_sub = db.relationship('Subscription', secondary=UE_SUB)
    
    def __init__(self, name, ip):
        self.name = name
        self.ue_ip = ip

    def __repr__(self):
        return '<UE %s %s>' % (self.name, self.ip)


class Subscription(db.Model):
    __tablename__ = 'subscription'
    name = db.Column(db.String(50), primary_key=True)
    port = db.Column(db.Integer)
    sub_server = db.relationship('Server', secondary=SUB_SERVER)
    
    def __init__(self, name, port):
        self.name = name
        self.port = port

    def __repr__(self):
        return '<Sub %s %s>' % (self.name, self.port)

class Server(db.Model):
    __tablename__ = 'server'
    ser_ip = db.Column(db.String(15), primary_key=True)
    
    def __init__(self, ip):
        self.ser_ip = ip

    def __repr__(self):
        return '<Server %s>' % (self.ip)
