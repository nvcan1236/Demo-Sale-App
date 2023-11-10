from flask import render_template, request, redirect
from app import app, login as saleapp_login
from flask_login import login_user
import dao


@app.route('/')
def index():
    kw = request.args.get('kw')
    cates = dao.get_categories()
    products = dao.get_products(kw)
    return render_template('index.html', categories=cates, products=products)


@app.route('/categories')
def category():
    cat_id = request.args.get('id')
    cates = dao.get_categories()
    products = dao.get_products_by_category(cat_id)
    return render_template('index.html', categories=cates, products=products)


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


if __name__ == '__main__':
    from app.admin import admin

    app.run(debug=True, port=5005)
