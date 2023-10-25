from flask import Flask, render_template

import dao

app = Flask(__name__)


@app.route('/')
def index():
    cates = dao.get_categories()
    products = dao.get_products()
    return render_template('index.html', categories=cates, products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5005)
