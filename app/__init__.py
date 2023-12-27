from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary

home_connect_string = "mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote("Myca@1236")
class_connect_string = "mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote("Admin@123")

app = Flask(__name__)
app.secret_key = 'DUKFHAKDGHNAK,DFHLDSKIFHALSK,JGDN ,KDFAJBN'
app.config["SQLALCHEMY_DATABASE_URI"] = class_connect_string
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 4
login = LoginManager(app=app)

cloudinary.config(
    cloud_name="dbd7vfk12",
    api_key="381798527745373",
    api_secret="mq7kD-ynrQsabeC3zUXc5zHuDIY"
)

db = SQLAlchemy(app=app)
