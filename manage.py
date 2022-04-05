# -*- coding: utf-8 -*-
# @Time    : 2022/4/5 12:34
# @Author  : Circleone_

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)