'''
Description: wx
Author: Monkee Lei
Date: 2021/11/15
'''
from http import HTTPStatus
from flask import Blueprint, request
from flasgger import swag_from
from api.schema.welcome import WelcomeSchema

wx_api = Blueprint('wx', __name__)


@wx_api.route('/echo')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the Flask Starter Kit',
            'schema': WelcomeSchema
        }
    }
})
def wx_echo():
    """
    微信echo回复接口
    返回echostr字符串传参
    ---
    """
    echostr = request.args.get('echostr', default='', type=str)
    return echostr, 200
