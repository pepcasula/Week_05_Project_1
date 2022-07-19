from flask import Blueprint, Flask, redirect, render_template, request

from models.ticket import Ticket
import repositories.ticket_repository as ticket_repository
import repositories.bug_repository as bug_repository
import repositories.product_repository as product_repository
import repositories.user_repository as user_repository

tickets_blueprint = Blueprint("tickets", __name__)

@tickets_blueprint.route("/ticket")
def ticket_menu():
    all_tickets = ticket_repository.select_all()
    return render_template("/ticket/index.html", all_tickets = all_tickets)

