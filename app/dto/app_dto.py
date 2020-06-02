from flask_restplus import Namespace, fields


class PayloadDTO:

    api = Namespace('api', description='api related operations')

    '''
     PUT PAYLOAD DTO
    '''

    PUTPayload = api.model('PutPayload', {
        "name": fields.String(example="scott")
    })


    '''
     POST PAYLOAD DTO
    '''

    POSTPayload = api.model('PostPayload', {
        "id":fields.Integer(example=1),
        "name": fields.String(example="scott")
    })