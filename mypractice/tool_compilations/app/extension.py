# -*- coding = utf-8 -*-
from apscheduler.schedulers.gevent import GeventScheduler
from flask_apscheduler import APScheduler
from flask_bcrypt import Bcrypt
# from flask_zipkin import Zipkin
from flask_login import LoginManager

# zipkin = Zipkin()
bcrypt = Bcrypt()
login_manager = LoginManager()

g = GeventScheduler()
apscheduler = APScheduler(scheduler=g)
