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
        bug = Bug(row['short_name'], row['description'], product, row['first_reported'], row['id'])
        bugs.append(bug)
    return bugs






