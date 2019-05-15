from rest_api_demo.database import db
from rest_api_demo.database.models import UE, Subscription, Server

## create UE
def create_ue(data):
    ue_id = data.get('ue_id')
    ue_name = data.get('name')
    ip = data.get('ip')
    ue = UE(ue_name, ip)
    db.session.add(ue)
    db.session.commit()

## create Subscription
def create_sub(data):
    sub_id = data.get('sub_id')
    sub_name = data.get('name')
    port = data.get('port')
    sub = Subscription(sub_id, sub_name, port)
    db.session.add(sub)
    db.session.commit()

## create Server
def create_ser(data):
    ser_id = data.get('ser_id')
    ip = data.get('ip')
    ser = Server(ser_id, ip)
    db.session.add(ser)
    db.session.commit()
    
## add link between UE and subscription
def update_ue_sub(ue_ip, data): 
    #ue_ip = data.get('ue_ip')
    name = data.get('name')
    ue = UE.query.filter(UE.ip == ue_ip).one()
    sub = Subscription.query.filter(Subscription.name == name).one()
    ue.ue_sub.append(sub)
    db.session.add(ue)
    db.session.commit()

## add link between subscription and server
def update_sub_server(name, data): 
    ip = data.get('ip')
    ser = Server.query.filter(Server.ip == ip).one()
    sub = Subscription.query.filter(Subscription.name == name).one()
    sub.sub_server.append(ser)
    db.session.add(sub)
    db.session.commit()
    
def delete_ue(ue_ip):
    ue = UE.query.filter(UE.ip == ue_ip).one()
    db.session.delete(ue)
    db.session.commit()

def delete_sub(sub_name):
    sub = Subscription.query.filter(Subscription.name == sub_name).one()
    db.session.delete(sub)
    db.session.commit()

def delete_ser(ser_ip):
    ser = Server.query.filter(Server.ip == ser_ip).one()
    db.session.delete(ser)
    db.session.commit()
    
'''
def create_sub(data):
    db.session.commit()

def create_UE_SUB(data):
    ue_id_br = data.get('ue_id')
    sub_id_br = data.get('sub_id')
    ue_sub = UE_SUB(ue_id_br, sub_id_br)
    db.session.add(ue_sub)
    db.session.commit()
'''    
'''
def create_blog_post(data):
    title = data.get('title')
    body = data.get('body')
    category_ip = data.get('category_ip')
    category = Category.query.filter(Category.ip == category_ip).one()
    post = Post(title, body, category)
    db.session.add(post)
    db.session.commit()


def update_post(post_id, data):
    post = Post.query.filter(Post.id == post_id).one()
    post.title = data.get('title')
    post.body = data.get('body')
    category_ip = data.get('category_ip')
    post.category = Category.query.filter(Category.ip == category_ip).one()
    db.session.add(post)
    db.session.commit()


def delete_post(post_id):
    post = Post.query.filter(Post.id == post_id).one()
    db.session.delete(post)
    db.session.commit()


def create_category(data):
    name = data.get('name')
    category_ip = data.get('ip')

    category = Category(name)
    if category_ip:
        category.ip = category_ip

    db.session.add(category)
    db.session.commit()


def update_category(category_ip, data):
    category = Category.query.filter(Category.ip == category_ip).one()
    category.name = data.get('name')
    db.session.add(category)
    db.session.commit()


def delete_category(category_ip):
    category = Category.query.filter(Category.ip == category_ip).one()
    db.session.delete(category)
    db.session.commit()
'''
