# -*- coding:utf-8 -*-
__author__ = 'gjw'
__date__ = '2018/9/22 16:19'

from flask import Blueprint

route_index = Blueprint("index_page",__name__)


@route_index.route("/")
def index():
    return "hello world"
