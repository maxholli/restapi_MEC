from flask_restplus import fields
from rest_api_demo.api.restplus import api

ue_add = api.model('ue add', {
    'name': fields.String(description='Name of the UE'),
    'ue_ip': fields.String(description='IP of the UE'),
})

sub_add = api.model('sub add', {
    'name': fields.String(description='Name of the subscription'),
    'port': fields.Integer(description='Port of the subscription'),    
})

ser_add = api.model('ser add', {
    'ser_ip': fields.String(description='IP of the server'),

})

ue_sub = api.model('ue sub', {
    'name': fields.String(readOnly=True, description='Name of the subscription'),
})

#sub_server = api.model('sub server', {
#    'ip': fields.String(readOnly=True, description='IP of the server'),
#})

## get a list of the subscriptions for a UE
ue_with_subs = api.inherit('UE with list of subscriptions', ue_add, {
    'ue_sub': fields.List(fields.Nested(sub_add)) ## 'ue_sub' has to correspond to a field in the UE object?? question?
})

sub_with_servers = api.inherit('Subscription with list of servers', sub_add, {
    'sub_server': fields.List(fields.Nested(ser_add))
})

ue_with_subs_servers = api.inherit('UE with list of subs and servers', ue_add, {
    'ue_sub': fields.List(fields.Nested(sub_with_servers))
})

