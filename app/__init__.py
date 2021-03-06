import os
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
db = MongoEngine(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from app import views, models


