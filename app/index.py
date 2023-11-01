from flask import render_template, request
from app import app
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
    return  render_template('index.html', categories=cates, products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5005)
