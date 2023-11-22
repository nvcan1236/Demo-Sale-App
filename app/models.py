from datetime import datetime
from app import db, app
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean, Enum
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from enum import Enum as UserEnum


class UserRole(UserEnum):
    ADMIN = 1
    USER = 2


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(255))
    category__id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(30), nullable=False)
    username = Column(String(30), default='user' + id)
    # is_active = Column(Boolean, default=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(255))
    create_at = Column(String(100), default=datetime.now())
    user_role = Column(Enum(UserRole), default=UserRole.USER)

    def __str__(self):
        return self.username


def create_init_category():
    cats = ['Điện thoại', 'Laptop', 'Tablet']
    for cat in cats:
        c = Category(name=cat)
        db.session.add(c)
        db.session.commit()


def create_init_products():
    products = [
        {
            'id': 1,
            'price': 32000000,
            'name': 'Z Flip5',
            'image': 'https://images.samsung.com/is/image/samsung/assets/vn/2307/pcd/PCD_B5_Whats-new_684X684_pc_alt.jpg?$684_684_JPG$',
            'cat_id': 1,
        },
        {
            'id': 2,
            'name': 'Galaxy Z Fold5',
            'price': 32000000,
            'image': 'https://images.samsung.com/is/image/samsung/assets/vn/2307/pcd/PCD_Q5_Whats-new_330x330_pc_alt.png?$330_330_PNG$',
            'cat_id': 1,
        },
        {
            'id': 3,
            'name': 'Galaxy S23 FE',
            'price': 32000000,
            'image': 'https://images.samsung.com/is/image/samsung/assets/vn/mobile/s23-fe/PCD_R11_Merchandising_376x376_pc.png?$160_160_PNG$',
            'cat_id': 2,
        },
        {
            'id': 4,
            'name': 'Galaxy S23 Ultra',
            'price': 32000000,
            'image': 'https://images.samsung.com/is/image/samsung/assets/vn/2307/pcd/PCD_DM3_KV_Whats-new_160x160_pc.png?$160_160_PNG$',
            'cat_id': 3,
        },
        {
            'id': 5,
            'name': 'Galaxy S23/ S23+',
            'price': 32000000,
            'image': 'https://images.samsung.com/is/image/samsung/assets/vn/2307/pcd/PCD_DM1_DM2_KV_Whats-new_160x160_pc.png?$160_160_PNG$',
            'cat_id': 2,
        },
        {
            'id': 6,
            'name': 'iPhone 15',
            'price': 32000000,
            'image': 'https://mobileleb.com/cdn/shop/files/apple-mobile-phone-apple-iphone-15-pro-max-512gb-33291439046788_1024x1024.jpg?v=1694771068',
            'cat_id': 3,
        },
    ]

    for product in products:
        p = Product()
        p.name = product['name']
        p.price = product['price']
        p.image = product['image']
        p.category__id = product['cat_id']
        db.session.add(p)
        db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        create_init_category()
        create_init_products()

        db.create_all()
