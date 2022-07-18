from db.run_sql import run_sql

from models.product import Product
from models.bug import Bug
from models.ticket import Ticket
from models.user import User
import repositories.product_repository as product_repository
import repositories.bug_repository as bug_repository
import repositories.ticket_repository as ticket_repository
import repositories.user_repository as user_repository

def save(product):
    sql = "INSERT INTO products (name) VALUES (%s) RETURNING *"
    values = [product.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product

def select_all():
    products = []
    sql = "SELECT * FROM products"
    results = run_sql(sql)
    for row in results:
        product = Product(row['name'], row['id'])
        products.append(product)

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE ID = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        product = Product(result['name'], result['id'])
        return product