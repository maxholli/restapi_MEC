import logging

from flask import request
from flask_restplus import Resource
## TODO: Make mec.business DONE, create_UE_SUB DONE, create_ue DONE, create_sub DONE
#from rest_api_demo.api.blog.business import create_category, delete_category, update_category
from rest_api_demo.api.mec.business import create_ue
## TODO: mec.serializers, ue_sub
#from rest_api_demo.api.blog.serializers import category, category_with_posts
from rest_api_demo.api.mec.serializers import ue_add
from rest_api_demo.api.restplus import api
## TODO: UE_SUB DONE, Subscription DONE, UE DONE 
from rest_api_demo.database.models import Subscription, UE

log = logging.getLogger(__name__)

ns = api.namespace('mec/ue', description='Operations related to UEs')

@ns.route('/')
class UE_Collection(Resource):

    @api.marshal_list_with(ue_add)
    def get(self):
        """
        Returns list of UEs.
        """
        ue = UE.query.all()
        #print(ue)
        return ue

    @api.response(201, 'Category successfully created.')
    @api.expect(ue_add)
    def post(self):
        """
        Creates a new UE.
        """
        data = request.json
        create_ue(data)
        return None, 201

'''
@ns.route('/<string:ip>')
@api.response(404, 'Category not found.')
class CategoryItem(Resource):

    @api.marshal_with(category_with_posts)
    def get(self, ip):
        """
        Returns a category with a list of posts.
        """
        return Category.query.filter(Category.ip == ip).one()

    @api.expect(category)
    @api.response(204, 'Category successfully updated.')
    def put(self, ip):
        """
        Updates a blog category.

        Use this method to change the name of a blog category.

        * Send a JSON object with the new name in the request body.

        ```
        {
          "name": "New Category Name"
        }
        ```

        * Specify the ID of the category to modify in the request URL path.
        """
        data = request.json
        update_category(ip, data)
        return None, 204

    @api.response(204, 'Category successfully deleted.')
    def delete(self, ip):
        """
        Deletes blog category.
        """
        delete_category(ip)
        return None, 204
'''
