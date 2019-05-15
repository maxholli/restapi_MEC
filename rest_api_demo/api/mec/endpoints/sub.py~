import logging

from flask import request
from flask_restplus import Resource
## TODO: Make mec.business DONE, create_UE_SUB DONE, create_ue DONE, create_sub DONE
#from rest_api_demo.api.blog.business import create_category, delete_category, update_category
from rest_api_demo.api.mec.business import create_ue, update_ue_sub, delete_ue
## TODO: mec.serializers, ue_sub
#from rest_api_demo.api.blog.serializers import category, category_with_posts
from rest_api_demo.api.mec.serializers import ue_add, ue_sub, ue_with_subs
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


@ns.route('/<string:ip>')
@api.response(404, 'UE not found.')
class UEItem(Resource):

    @api.marshal_with(ue_add)
    def get(self, ip):
        """
        Returns a name of UE associated with an IP.
        """
        return UE.query.filter(UE.ip == ip).one()

    @api.expect(ue_sub)
    @api.response(204, 'UE successfully updated.')
    def put(self, ip):
        """
        Updates a UE - Subscription relation.

        Use this method to add a subscription to the UE.

        * Send a JSON object with the new subcription name.

        ```
        {
          "sub_name": "New Subscription Name"
        }
        ```

        * Specify the IP of the UE to modify in the request URL path.
        """
        data = request.json
        update_ue_sub(ip, data)
        return None, 204

    @api.response(204, 'UE successfully deleted.')
    def delete(self, ip):
        """
        Deletes UE.
        """
        delete_ue(ip)
        return None, 204

@ns.route('/<string:ip>/subs')
@api.response(404, 'UE not found.')
class UEsubs(Resource):

    @api.marshal_with(ue_with_subs)
    def get(self, ip):
        """
        Returns all subscriptions associated with an IP.
        """
        return UE.query.filter(UE.ip == ip).one()
