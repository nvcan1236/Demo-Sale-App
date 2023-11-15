from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

home_connect_string = "mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote("Myca@1236")
class_connect_string = "mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote("Admin@123")

app = Flask(__name__)
app.secret_key = 'DUKFHAKDGHNAK,DFHLDSKIFHALSK,JGDN ,KDFAJBN'
app.config["SQLALCHEMY_DATABASE_URI"] = home_connect_string
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 4
login = LoginManager(app=app)

db = SQLAlchemy(app=app)

