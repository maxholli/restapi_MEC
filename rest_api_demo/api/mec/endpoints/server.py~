import logging

from flask import request
from flask_restplus import Resource
## TODO: Make mec.business DONE, create_UE_SUB DONE, create_ue DONE, create_sub DONE
#from rest_api_demo.api.blog.business import create_category, delete_category, update_category
from rest_api_demo.api.mec.business import create_ue, update_ue_sub, delete_ue, create_sub, delete_sub, update_sub_server
## TODO: mec.serializers, ue_sub
#from rest_api_demo.api.blog.serializers import category, category_with_posts
from rest_api_demo.api.mec.serializers import ue_add, ue_sub, ue_with_subs, sub_add, sub_with_servers, sub_server
from rest_api_demo.api.restplus import api
## TODO: UE_SUB DONE, Subscription DONE, UE DONE 
from rest_api_demo.database.models import Subscription, UE

log = logging.getLogger(__name__)

ns = api.namespace('mec/subscription', description='Operations related to Subscriptions')

@ns.route('/')
class Sub_Collection(Resource):

    @api.marshal_list_with(sub_add)
    def get(self):
        """
        Returns list of Subscriptions.
        """
        sub = Subscription.query.all()
        #print(ue)
        return sub

    @api.response(201, 'Subscription successfully created.')
    @api.expect(sub_add)
    def post(self):
        """
        Creates a new Subscription.
        """
        data = request.json
        create_sub(data)
        return None, 201


@ns.route('/<string:name>')
@api.response(404, 'Subscription not found.')
class SubItem(Resource):

    @api.marshal_with(sub_add)
    def get(self, name):
        """
        Returns info associated with a subscription name.
        """
        return Subscription.query.filter(Subscription.name == name).one()

    @api.expect(sub_server)
    @api.response(204, 'Subscription successfully updated.')
    def put(self, name):
        """
        Updates a Subscription - Server relation.

        Use this method to add a server to the Subscription.

        * Send a JSON object with the new server IP.

        ```
        {
          "ip": "New Server IP"
        }
        ```

        * Specify the name of the Subscription to modify in the request URL path.
        """
        data = request.json
        update_sub_server(name, data)
        return None, 204
    
    @api.response(204, 'Subscription successfully deleted.')
    def delete(self, name):
        """
        Deletes Subscription.
        """
        delete_sub(name)
        return None, 204

@ns.route('/<string:name>/servers')
@api.response(404, 'Subscription not found.')
class SubServers(Resource):

    @api.marshal_with(sub_with_servers)
    def get(self, name):
        """
        Returns all servers associated with a subscription.
        """
        return Subscription.query.filter(Subscription.name == name).one()
