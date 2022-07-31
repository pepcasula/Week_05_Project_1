from crypt import methods
from flask import Blueprint, Flask, redirect, render_template, request

from models.bug import Bug

import repositories.bug_repository as bug_repository
import repositories.product_repository as product_repository
import repositories.ticket_repository as ticket_repository
import repositories.user_repository as user_repository

bugs_blueprint = Blueprint("bugs", __name__)

@bugs_blueprint.route("/bug")
def bug_menu():
    return render_template("/bug/index.html")

@bugs_blueprint.route("/bug_info")
def get_all_bugs():
    all_bugs = bug_repository.select_all()
    return render_template("/bug_info/index.html", all_bugs = all_bugs)

@bugs_blueprint.route("/bug_info/by_product", methods=['POST'])
def get_by_product():
    product = request.form['product']
    all_bugs = bug_repository.select_all_by_product(product)
    return render_template("/bug_info/by_product.html", all_bugs = all_bugs)

@bugs_blueprint.route("/bug_info/new", methods=['POST'])
def add_new_bug():
    bugname = request.form['short_name']
    bugdescription = request.form['description']
    bugproduct = request.form['product_id']
    bugproduct_id = product_repository.select(bugproduct)
    bugdate = request.form['first_reported']
    new_bug = Bug(bugname, bugdescription, bugproduct_id, bugdate)
    bug_repository.save(new_bug)
    return render_template("/bug_info/new.html", new_bug = new_bug)

