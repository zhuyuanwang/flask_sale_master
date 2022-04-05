# -*- coding: utf-8 -*-
# @Time    : 2022/4/5 12:42
# @Author  : Circleone_

from flask import Flask
from flask_login import LoginManager

def register_web_blueprint(app):
    from app.web import web
    app.register_blueprint(web)

def create_app(config=None):
    app = Flask(__name__)

    app.config.from_object('app.settings')
    app.config.from_object('app.secure')
    # app.config.from_object('app.config')
    register_web_blueprint(app)

    return app