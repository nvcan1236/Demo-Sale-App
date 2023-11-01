from app.models import Category, Product


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
