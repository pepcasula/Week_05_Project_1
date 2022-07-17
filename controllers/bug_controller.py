from flask import Blueprint, Flask, redirect, render_template, request

from models.bug import Bug
import repositories.bug_repository as bug_repository
import repositories.product_repository as product_repository
import repositories.ticket_repository as ticket_repository
import repositories.user_repository as user_repository

bugs_blueprint = Blueprint("bugs", __name__)

@bugs_blueprint.route("/bug")
def bug_info():
    return render_template("bug/index.html")
