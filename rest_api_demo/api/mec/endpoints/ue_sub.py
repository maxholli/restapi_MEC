import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.mec.business import create_ue, update_ue_sub, delete_ue, delete_all_ues
from rest_api_demo.api.mec.serializers import ue_add, ue_sub, ue_with_subs, ue_with_subs_servers
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import UE

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

    @api.response(201, 'UE successfully created.')
    @api.expect(ue_add)
    def post(self):
        """
        Creates a new UE.
        """
        data = request.json
        create_ue(data)
        return None, 201

    @api.response(204, 'All UEs successfully deleted.')
    def delete(self):
        """
        Deletes all UEs.
        """
        ues = UE.query.all()
        delete_all_ues(ues)
        return None, 204

@ns.route('/<string:ip>')
@api.response(404, 'UE not found.')
class UEItem(Resource):

    @api.marshal_with(ue_add)
    def get(self, ip):
        """
        Returns a name of UE associated with an IP.
        """
        return UE.query.filter(UE.ue_ip == ip).one()

    @api.expect(ue_sub)
    @api.response(204, 'UE successfully updated.')
    def put(self, ip):
        """
        Updates a UE - Subscription relation.

        Use this method to add a subscription to the UE.

        * Send a JSON object with the new subcription name.

        ```
        {
          "name": "New Subscription Name"
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
        Deletes specified UE.
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
        return UE.query.filter(UE.ue_ip == ip).one()

@ns.route('/<string:ip>/subsciption_servers')
@api.response(404, 'UE not found.')
class UEsubs_servers(Resource):

    @api.marshal_with(ue_with_subs_servers)
    def get(self, ip):
        """
        Returns all subscriptions and their servers associated with an UE.
        """
        return UE.query.filter(UE.ue_ip == ip).one()
