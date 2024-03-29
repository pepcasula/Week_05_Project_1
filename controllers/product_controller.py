from flask import Blueprint, Flask, redirect, render_template, request

from models.product import Product
import repositories.product_repository as product_repository
import repositories.bug_repository as bug_repository
import repositories.ticket_repository as ticket_repository
import repositories.user_repository as user_repository

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/product")
def product_info():
    return render_template("product/index.html")

@products_blueprint.route("/product_info")
def get_all_products():
    all_products = product_repository.select_all()
    return render_template("product_info/index.html", all_products = all_products)

@products_blueprint.route("/product_info/new", methods=['POST'])
def add_new_product():
    productname = request.form['name']
    new_product = Product(productname)
    product_repository.save(new_product)
    return render_template("product_info/new.html", new_product=new_product)