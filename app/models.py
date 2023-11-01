from app import db, app
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(255))
    category__id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        p = Product()
        p.name = 'iPhone 15'
        p.price = 32000000
        p.image = 'https://mobileleb.com/cdn/shop/files/apple-mobile-phone-apple-iphone-15-pro-max-512gb-33291439046788_1024x1024.jpg?v=1694771068'
        p.category__id=1
        db.session.add(p)
        db.session.commit()

        db.create_all()
