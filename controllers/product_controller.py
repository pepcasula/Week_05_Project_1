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


