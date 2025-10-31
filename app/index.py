from itertools import product
from flask import render_template,request
from app import dao,app
import math

@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    page = request.args.get("page")
    products = dao.load_products(q=q, cate_id=cate_id,page=page)
    pages = math.ceil(dao.count_product()/app.config["PAGE_SIZE"])
    return render_template("index.html",products=products, pages=pages)

@app.route("/products/<int:id>")
def detail(id):
    return render_template("product_detail.html",p=dao.get_product_by_id(id))

def print_acc_info(tk,mk):
    print(tk)
    print(mk)


@app.route("/login")
def login():
    tk = request.args.get("tk")
    mk = request.args.get("mk")
    return render_template("login.html",tk=tk, mk=mk)

@app.context_processor
def common_attribute():
    return {
        "categories": dao.load_categories()
    }

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
