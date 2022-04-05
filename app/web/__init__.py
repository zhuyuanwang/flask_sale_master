# -*- coding: utf-8 -*-
# @Time    : 2022/4/5 12:47
# @Author  : Circleone_

from flask import Blueprint

web = Blueprint('web', __name__, template_folder='templates')

from app.web import main
