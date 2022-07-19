from flask import Blueprint, Flask, redirect, render_template, request

from models.user import User
import repositories.user_repository as user_repository
import repositories.bug_repository as bug_repository
import repositories.product_repository as product_repository
import repositories.ticket_repository as ticket_repository

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/")
def user_home():
    return render_template("index.html")

@users_blueprint.route("/user_tech")
def user_tech_menu():
    return render_template("user_tech/index.html")

@users_blueprint.route("/user_dev")
def user_dev_menu():
    return render_template("user_dev/index.html")

@users_blueprint.route("/user_adm")
def user_adm_menu():
    return render_template("user_adm/index.html")

@users_blueprint.route("/user_info")
def get_all_users():
    all_users = user_repository.select_all()
    return render_template("user_info/index.html", all_users = all_users)

# @users_blueprint.route("/user_info/new")
# def add_new_user():
#     return render_template("user_info/new.html")