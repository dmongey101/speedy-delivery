from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)

login = LoginManager(app)
login.init_app(app)

# from app import models
# from app.admin import AdminIndexView, CustomAdminView

# admin = Admin(app, name='Speedy Delivery', index_view=AdminIndexView(),
#               template_mode='bootstrap3')