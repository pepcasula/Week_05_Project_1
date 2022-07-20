from flask import Blueprint, Flask, redirect, render_template, request

from models.user import User
import repositories.user_repository as user_repository
import repositories.bug_repository as bug_repository
import repositories.product_repository as product_repository
import repositories.ticket_repository as ticket_repository

users_blueprint = Blueprint("users", __name__)

USER_TYPES = [
    'Tech Support',
    'Developer',
    'System Admin'
]

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
    all_users = user_repository.select_all()
    return render_template("user_adm/index.html", all_users = all_users)

@users_blueprint.route("/user_info")
def get_all_users():
    all_users = user_repository.select_all()
    return render_template("user_info/index.html", all_users = all_users, user_types = USER_TYPES)

@users_blueprint.route("/user_info/new", methods=['POST'])
def add_new_user():
    username = request.form['name']
    usertype = request.form['type']
    new_user = User(username, usertype)
    user_repository.save(new_user)
    return render_template("user_info/new.html", new_user=new_user)

@users_blueprint.route("/user_info/edit", methods=['UPDATE'])
def edit_user():
    username = request.form['name']
    usertype = request.form['type']
    userid = request.form['user_id']
    edit_user = User(username, usertype, userid)  
    user_repository.update(edit_user)
    return render_template("user_info/edit.html")


    