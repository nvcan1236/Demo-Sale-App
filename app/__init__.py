from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy

home_connect_string = "mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote("Myca@1236")
class_connect_string = "mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote("Admin@123")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = home_connect_string
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)

