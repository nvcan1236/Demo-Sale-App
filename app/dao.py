import hashlib
from app.models import Category, Product, User
from app import db


def get_categories():
    return Category.query.all()


def get_products_by_category(id):
    products = Product.query.filter(Product.category__id == id)

    return products


def get_products(kw):
    products = Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))

    return products.all()


def create_user(username, email, password):
    u = User()
    u.username = username
    u.email = email
    u.password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    db.session.add(u)
    db.session.commit()


def check_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = User.query.filter(User.username.__eq__(username.strip()),
                          User.password.__eq__(password)).first()

    if u:
        print(password)
        return u


def get_user_by_id(user_id):
    return User.query.get(user_id)
