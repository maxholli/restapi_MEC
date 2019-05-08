from rest_api_demo.database import db
from rest_api_demo.database.models import Post, Category


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
