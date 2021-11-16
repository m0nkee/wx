'''
Description: 
Author: Monkee Lei
Date: 2021/11/15
'''
from flask import Flask
from flasgger import Swagger
from api.route.home import home_api
from api.route.wx import wx_api

def create_app():
    app = Flask(__name__)

    app.config['SWAGGER'] = {
        'title': 'Flask API Starter Kit',
    }
    swagger = Swagger(app)
     ## Initialize Config
    app.config.from_pyfile('config.py')
    app.register_blueprint(home_api, url_prefix='/api')
    app.register_blueprint(wx_api, url_prefix='/wx')

    return app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host='0.0.0.0', port=port)
