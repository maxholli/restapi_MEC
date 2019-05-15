from flask_restplus import fields
from rest_api_demo.api.restplus import api

ue_add = api.model('ue add', {
    'ue_id': fields.Integer(readOnly=True, description='The unique id for UE'),
    'name': fields.String(description='Name of the UE'),
    'ip': fields.String(description='IP of the UE'),
})

sub_add = api.model('sub add', {
    'sub_id': fields.Integer(readOnly=True, description='The unique id for sub'),
    'name': fields.String(description='Name of the subscription'),
    'port': fields.Integer(description='Port of the subscription'),    
})

ue_sub = api.model('ue sub', {
    'name': fields.String(readOnly=True, description='Name of the subscription'),
    #'ue_ip': fields.Integer(readOnly=True, description='IP of the UE'),
})

## get a list of the subscriptions for a UE
ue_with_subs = api.inherit('UE with list of subscriptions', ue_add, {
    'ue_sub': fields.List(fields.Nested(sub_add))
})

'''
blog_post = api.model('Blog post', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a blog post'),
    'title': fields.String(required=True, description='Article title'),
    'body': fields.String(required=True, description='Article content'),
    'pub_date': fields.DateTime,
    'category_ip': fields.String(attribute='category.ip'),
    'category': fields.String(attribute='category.name'),
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_blog_posts = api.inherit('Page of blog posts', pagination, {
    'items': fields.List(fields.Nested(blog_post))
})

category = api.model('Blog category', {
    'ip': fields.String(readOnly=True, description='The unique identifier of a blog category'),
    'name': fields.String(required=True, description='Category name'),
})

category_with_posts = api.inherit('Blog category with posts', category, {
    'posts': fields.List(fields.Nested(blog_post))
})
'''
