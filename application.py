# -*- coding:utf-8 -*-
import os

__author__ = 'gjw'
__date__ = '2018/9/22 15:24'

from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy


class Application(Flask):
    def __init__(self, import_name):
        super(Application, self).__init__(import_name)
        self.config.from_pyfile('config/base_setting.py')
        if "ops_config" in os.environ:
            self.config.from_pyfile("config/%s_setting.py"%os.environ["ops_config"])

        db.init_app(self)


db = SQLAlchemy()
app = Application(__name__)
manager = Manager(app)


