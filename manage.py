# -*- coding:utf-8 -*-
__author__ = 'gjw'
__date__ = '2018/9/22 15:27'

from application import app,manager
from flask_script import Server
import www

# web server
manager.add_command("runserver", Server(host="0.0.0.0",port=5000,use_debugger=True,use_reloader=True))


def main():
    app.run()


if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()