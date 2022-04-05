# -*- coding: utf-8 -*-
# @Time    : 2022/4/5 12:48
# @Author  : Circleone_

import datetime
from . import web

@web.route('/')
def index():
    return "hello zyw：{}".format(datetime.datetime.now())