import json
from turtledemo.penrose import start

from app import app
from models import Category, Product


def load_categories():
    # with open("data/categories.json",encoding="utf-8") as c:
    #     return json.load(c)
    return Category.query.all()

def load_products(q=None,cate_id=None,page=None):
    # with open("data/products.json",encoding="utf-8") as p:
    #     products = json.load(p)
    #     if q:
    #         products = [p for p in products if p["name"].find(q)>=0]
    #
    #     if cate_id:
    #         products = [p for p in products if p["cate_id"].__eq__(int(cate_id))]
    #
    #     return products
    query = Product.query

    if q:
        query = query.filter(Product.name.contains(q))

    if cate_id:
        query = query.filter(Product.category_id.__eq__(cate_id))

    if page:
        size = app.config["PAGE_SIZE"]
        start = (int(page)-1)*size
        query = query.slice(start, start+size)

    return query.all()

def count_product():
    return Product.query.count()

def get_product_by_id(id):
    # with (open("data/products.json",encoding="utf-8") as p):
    #     products = json.load(p)
    #
    #     for p in products:
    #         if p["id"].__eq__(id):
    #             return p
    return Product.query.get(id)

    return None