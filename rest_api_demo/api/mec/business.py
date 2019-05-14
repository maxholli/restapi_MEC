from rest_api_demo.database import db
from rest_api_demo.database.models import UE, Subscription

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
    sub_name = data.get('sub_name')
    port = data.get('sub_port')
    sub = Subscription(sub_id, sub_name, port)
    db.session.add(sub)
    db.session.commit()
    
## add link between UE and subscription
def update_ue_sub(data): 
    ue_ip = data.get('ue_ip')
    name = data.get('sub_name')
    ue = UE.query.filter(UE.ip == ue_ip).one()
    sub = Subscription.query.filter(Subscription.name == name).one()
    ue.ue_sub.append(sub)
    db.session.add(ue)
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
