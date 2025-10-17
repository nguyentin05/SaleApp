import json

def load_categories():
    with open("data/categories.json",encoding="utf-8") as c:
        return json.load(c)

def load_products(q=None,cate_id=None):
    with open("data/products.json",encoding="utf-8") as p:
        products = json.load(p)
        if q:
            products = [p for p in products if p["name"].find(q)>=0]

        if cate_id:
            products = [p for p in products if p["cate_id"].__eq__(int(cate_id))]

        return products

def get_product_by_id(id):
    with (open("data/products.json",encoding="utf-8") as p):
        products = json.load(p)

        for p in products:
            if p["id"].__eq__(id):
                return p

    return None