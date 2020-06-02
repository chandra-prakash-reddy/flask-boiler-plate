from app.dto.app_dto import PayloadDTO
from app.handler.error import create_error_response
from app.handler.http import create_response
from common.app_logger import AppLogger
from flask_restplus import Resource
from flask import request

logger = AppLogger.instance().logger
api = PayloadDTO.api
_put_payload = PayloadDTO.PUTPayload
_post_payload = PayloadDTO.POSTPayload

authentication = api.parser().add_argument('Authorization', type=str, location='headers', help='', required=True)


@api.route('')
@api.response(500, 'Internal Server error.')
class BoilerPlateDemoPost(Resource):

    @api.expect(_post_payload, validate=True)
    def post(self):
        """post id"""
        logger.info("requested data : {} ".format(request.json))
        try:
            return create_response(request.json,
                                   status_code=201)
        except Exception as e:
            return create_error_response(e)


@api.route('/<id>')
@api.param(name='id', description='Identifier', _in='path', type='String', required='true')
@api.response(404, 'id not found.')
@api.response(500, 'Internal Server error.')
class BoilerPlateRestDemo(Resource):

    def get(self, id):
        """get id"""
        logger.info("requested id : {} ".format(id))
        try:
            return create_response({'id': id},
                                   status_code=200)
        except Exception as e:
            return create_error_response(e)

    @api.expect(_put_payload, validate=True)
    def put(self, id):
        """update id"""
        logger.info("requested data : {} ".format(request.json))
        data = request.json
        data['id'] = id
        try:
            return create_response(data=data,
                                   status_code=200)
        except Exception as e:
            return create_error_response(e)

    def delete(self, id):
        """delete id"""
        logger.info("deleting id : {} ".format(id))
        try:
            return create_response({'id': id},
                                   status_code=200)
        except Exception as e:
            return create_error_response(e)
