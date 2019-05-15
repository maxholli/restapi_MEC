import logging

from flask import request
from flask_restplus import Resource
## TODO: Make mec.business DONE, create_UE_SUB DONE, create_ue DONE, create_sub DONE
#from rest_api_demo.api.blog.business import create_category, delete_category, update_category
from rest_api_demo.api.mec.business import create_ue, update_ue_sub, delete_ue, create_sub, delete_sub, update_sub_server, create_ser, delete_ser
## TODO: mec.serializers, ue_sub
#from rest_api_demo.api.blog.serializers import category, category_with_posts
from rest_api_demo.api.mec.serializers import ue_add, ue_sub, ue_with_subs, sub_add, sub_with_servers, sub_server, ser_add
from rest_api_demo.api.restplus import api
## TODO: UE_SUB DONE, Subscription DONE, UE DONE 
from rest_api_demo.database.models import Subscription, UE, Server

log = logging.getLogger(__name__)

ns = api.namespace('mec/server', description='Operations related to Servers')

@ns.route('/')
class Server_Collection(Resource):

    @api.marshal_list_with(ser_add)
    def get(self):
        """
        Returns list of Servers.
        """
        ser = Server.query.all()
        return ser

    @api.response(201, 'Server successfully created.')
    @api.expect(ser_add)
    def post(self):
        """
        Creates a new Server.
        """
        data = request.json
        create_ser(data)
        return None, 201


@ns.route('/<string:ip>')
@api.response(404, 'Server not found.')
class SerItem(Resource):

    @api.marshal_with(ser_add)
    def get(self, ip):
        """
        Returns info associated with a server.
        """
        return Server.query.filter(Server.ip == ip).one()

    
    @api.response(204, 'Server successfully deleted.')
    def delete(self, ip):
        """
        Deletes Server.
        """
        delete_ser(ip)
        return None, 204
