from itertools import product

from flask import Flask, render_template,request
from app import dao

app = Flask(__name__)

@app.route("/")
def index():
    q= request.args.get("q")
    cate_id = request.args.get("cate_id")
    cates = dao.load_categories()
    products = dao.load_products(q=q, cate_id=cate_id)
    return render_template("index.html",cates = cates,products=products)

@app.route("/products/<int:id>")
def detail(id):
    cates = dao.load_categories()
    return render_template("product_detail.html",p=dao.get_product_by_id(id),cates=cates)

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)