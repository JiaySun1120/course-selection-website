# -*- coding: utf-8 -*-

import sys
sys.path.append('./src')

from flask import Flask, redirect, url_for
from gevent import pywsgi
from admin import admin_bp
from student import student_bp
from teacher import teacher_bp
from edit import edit_bp
from data_get import data_bp
from login_logout import log_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'xgmdRrFe.323'

app.register_blueprint(admin_bp)
app.register_blueprint(student_bp)
app.register_blueprint(teacher_bp)
app.register_blueprint(edit_bp)
app.register_blueprint(data_bp)
app.register_blueprint(log_bp)


# 根路由
@app.route('/', methods=['GET', 'POST'])
def home():
    # print('here')
    return redirect(url_for('log.login'))


# 主函数
if __name__ == '__main__':
    # print(app.url_map)
    # app.run(host='127.0.0.1', port = 5000,debug=True)
    app.run(debug=True)
    server = pywsgi.WSGIServer(('', 5000), app)
    server.serve_forever()
