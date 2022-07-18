from db.run_sql import run_sql

from models.ticket import Ticket
from models.bug import Bug
from models.product import Product
from models.user import User
import repositories.ticket_repository as ticket_repository
import repositories.bug_repository as bug_repository
import repositories.product_repository as product_repository
import repositories.user_repository as user_repository

def save(ticket):
    sql = "INSERT INTO tickets (bug_id, product_id, date_subm, user_id, ticket_status) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [
        ticket.bug.id,
        ticket.product.id,
        ticket.date_subm,
        ticket.user.id,
        ticket.ticket_status
        ]
    results = run_sql(sql, values)
    id = results[0]['id']
    ticket.id = id
    return ticket