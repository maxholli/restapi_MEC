import logging

from flask import request
from flask_restplus import Resource

from rest_api_demo.api.mec.business import create_ser, delete_ser
from rest_api_demo.api.mec.serializers import ser_add
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import Server

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
        return Server.query.filter(Server.ser_ip == ip).one()

    
    @api.response(204, 'Server successfully deleted.')
    def delete(self, ip):
        """
        Deletes Server.
        """
        delete_ser(ip)
        return None, 204
