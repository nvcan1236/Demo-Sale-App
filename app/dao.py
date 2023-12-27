import hashlib
from app.models import Category, Product, User, Receipt, ReceiptDetail
from app import db, app
from flask_login import current_user
from flask import request


def get_categories():
    return Category.query.all()


def get_products_by_category(id):
    products = Product.query.filter(Product.category_id == id)

    return products


def count_product():
    return Product.query.count()


def get_products(kw, cate_id, page=None):
    products = Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))

    if cate_id:
        products = products.filter(Product.category_id == cate_id)

    if page:
        page = int(page)
        page_size = app.config['PAGE_SIZE']
        start = (page - 1) * page_size
        products = products.slice(start, start + page_size)
        return products

    return products.all()


def create_user(username, email, password, avatar):
    u = User()
    u.username = username
    u.email = email
    u.password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    avatar = request.files.get('avatar')
    if avatar:
        cloudinary.uploader.upload(avatar)
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


def add_receipt(cart):
    if cart:
        r = Receipt(user=current_user)
        db.session.add(r)
        for i in cart.values():
            d = ReceiptDetail(receipt=r, product_id=i['id'], unit_price=i['price'], qty=i['quantity'])
            db.session.add(d)

        try:
            db.session.commit()
        except:
            return False
        else:
            return True

    return False

