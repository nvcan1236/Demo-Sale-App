import json
import math

from flask import render_template, request, redirect, jsonify, session
from app import app, login as saleapp_login
from flask_login import login_user
import dao
import utils


@app.context_processor
def common_response():
    return {
        'categories': dao.get_categories(),
        'cart': utils.count_cart(session.get('cart'))
    }

@app.route('/')
def index():
    kw = request.args.get('kw')
    page = request.args.get('page')
    cate_id = request.args.get('cate_id')
    products = dao.get_products(kw, cate_id, page)
    page_count = math.ceil(dao.count_product()/app.config['PAGE_SIZE'])
    return render_template('index.html', products=products, page_count=page_count)


@app.route('/cart')
def cart():
    return render_template('cart.html')

# @app.route('/categories')
# def category():
#     cat_id = request.args.get('id')
#     cates = dao.get_categories()
#     products = dao.get_products_by_category(cat_id)
#     return render_template('index.html', categories=cates, products=products)


@app.route('/admin/register', methods=['post'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_pw')
    if password == confirm_password:
        dao.create_user(username, email, password)
        return redirect('/admin')
    # else:
    #     render_template('/admin/index.html', pw_error='Mật khẩu không trùng khớp')


@app.route('/admin/login', methods=['post'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = dao.check_user(username=username, password=password)
    if user:
        login_user(user)

    return redirect('/admin')


@saleapp_login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id=user_id)


@app.route('/api/cart', methods=['post', 'patch', 'delete'])
def add_to_cart():

    data = request.json
    cart = session.get('cart')
    if cart is None:
        cart = {}

    if request.method == 'POST':
        id = str(data.get('id'))
        name = data.get('name')
        price = data.get('price')

        if id in cart:
            cart[id]['quantity'] += 1
        else:
            cart[id] = {
                'id': id,
                'name': name,
                'price': price,
                'quantity': 1
            }
    elif request.method == 'PATCH':
        id = str(data.get('id'))
        quantity = data.get('quantity')
        if id in cart:
            cart[id]['quantity'] = quantity

    elif request.method == 'DELETE':
        id = str(data.get('id'))
        if id in cart:
            del cart[id]

    session['cart'] = cart
    print(cart)
    return jsonify(utils.count_cart(cart))


if __name__ == '__main__':
    from app.admin import admin

    app.run(debug=True, port=5005)
