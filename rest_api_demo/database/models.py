# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

from datetime import datetime

from rest_api_demo.database import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    category_ip = db.Column(db.String(50), db.ForeignKey('category.ip'))
    category = db.relationship('Category', backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body, category, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    ip = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name

UE_SUB = db.Table('ue_sub',
                  db.Column('ue_id_br', db.Integer, db.ForeignKey('ue.ue_id'), primary_key=True),
                  db.Column('sub_id_br', db.Integer, db.ForeignKey('subscription.sub_id'), primary_key=True)
)

SUB_SERVER = db.Table('sub_server',
                  db.Column('ser_id_tr', db.Integer, db.ForeignKey('server.ser_id'), primary_key=True),
                  db.Column('sub_id_tr', db.Integer, db.ForeignKey('subscription.sub_id'), primary_key=True)
)
    
class UE(db.Model):
    __tablename__ = 'ue'
    ue_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ip = db.Column(db.String(15), unique=True, nullable=False)
    ue_sub = db.relationship('Subscription', secondary=UE_SUB)
    
    def __init__(self, name, ip):
        #self.ue_id = ue_id
        self.name = name
        self.ip = ip

    def __repr__(self):
        return '<UE %s %s>' % (self.name, self.ip)


class Subscription(db.Model):
    __tablename__ = 'subscription'
    sub_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    port = db.Column(db.Integer)
    sub_server = db.relationship('Server', secondary=SUB_SERVER)
    
    def __init__(self, sub_id, name, port):
        self.sub_id = sub_id
        self.name = name
        self.port = port

    def __repr__(self):
        return '<Sub %d %s %s>' % (self.sub_id, self.name, self.port)

class Server(db.Model):
    __tablename__ = 'server'
    ser_id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(15))
    
    def __init__(self, ser_id, ip):
        self.ser_id = ser_id
        self.ip = ip

    def __repr__(self):
        return '<Server %d %s>' % (self.ser_id, self.ip)
