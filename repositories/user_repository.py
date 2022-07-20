from db.run_sql import run_sql

from models.user import User
from models.ticket import Ticket
from models.bug import Bug
from models.product import Product
import repositories.user_repository as user_repository
import repositories.ticket_repository as ticket_repository
import repositories.bug_repository as bug_repository
import repositories.product_repository as product_repository

def save(user):
    sql = "INSERT INTO users (name, user_type) VALUES (%s, %s) RETURNING *"
    values = [
        user.name,
        user.user_type
    ]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user

def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        user = User(row['name'], row['user_type'], row['id'])
        users.append(user)
    return users

def select(id):
    user = None
    sql = "SELECT * FROM users WHERE ID = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        user = User(result['name'], result['user_type'], result['id'])
        return user 

    
