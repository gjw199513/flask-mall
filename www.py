# -*- coding:utf-8 -*-
__author__ = 'gjw'
__date__ = '2018/9/22 15:31'

from application import app
from web.controllers.index import route_index


app.register_blueprint(route_index, url_prefix="/")