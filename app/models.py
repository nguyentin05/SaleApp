import json

from app import db,app
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    products = relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(300),nullable=False)
    price = Column(Float, default=0.0)
    image = Column(String(300), default="https://cdnv2.tgdd.vn/mwg-static/tgdd/Products/Images/44/335362/macbook-air-13-inch-m4-11-638769622719537641-750x500.jpg")
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False )

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        with (open("data/products.json", encoding="utf-8") as p):
            products = json.load(p)

            for p in products:
                db.session.add(Product(**p))

        db.session.commit()