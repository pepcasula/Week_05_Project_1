from itertools import product
from db.run_sql import run_sql

from models.bug import Bug
from models.ticket import Ticket
from models.product import Product
from models.user import User
import repositories.bug_repository as bug_repository
import repositories.ticket_repository as ticket_repository
import repositories.product_repository as product_repository
import repositories.user_repository as user_repository

def save(bug):
    sql = "INSERT INTO bugs (short_name, description, product_id, first_reported) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [
        bug.short_name,
        bug.description,
        bug.product.id,
        bug.first_reported
        ]
    results = run_sql(sql, values)
    id = results[0]['id']
    bug.id = id
    return bug

def select_all():
    bugs = []
    sql = "SELECT * FROM bugs"
    results = run_sql(sql)
    for row in results:
        product = product_repository.select(row["product_id"])
        bug = Bug(row['short_name'], row['description'], product.name, row['first_reported'], row['id'])
        bugs.append(bug)
    return bugs

def select(id):
    bug = None
    sql = "SELECT * FROM bugs WHERE ID = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        product = product_repository.select(result["product_id"])
        bug = Bug(result['short_name'], result['description'], product.name, result['first_reported'], result['id'])
        return bug


def select_all_by_product(id):
    bugs = []
    sql = "SELECT * FROM bugs WHERE product_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        product = product_repository.select(row["product_id"])
        bug = Bug(row['short_name'], row['description'], product.name, row['first_reported'], row['id'])
        bugs.append(bug)
    return bugs

