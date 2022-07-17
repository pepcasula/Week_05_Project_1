import pdb

from models.ticket import Ticket
import repositories.ticket_repository as ticket_repository

from models.bug import Bug
import repositories.bug_repository as bug_repository

from models.product import Product
import repositories.product_repository as product_repository

from models.user import User
import repositories.user_repository as user_repository

# ticket_repository.delete_all()
# bug_repository.delete_all()
# product_repository.delete_all()
# user_repository.delete_all()

user1 = User("Pippo Lo Russo", "Admin")
user_repository.save(user1)

user2 = User("Leila Simmons", "Developer")
user_repository.save(user2)

user3 = User("Kyle Montgomery", "Developer")
user_repository.save(user3)

user4 = User("Laura Benitez", "Developer")
user_repository.save(user4)

user5 = User("Johann Van Sanchez", "Tech Support")
user_repository.save(user5)

user6 = User("Mia Stockwell", "Tech Support")
user_repository.save(user6)

user7 = User("Luis Perez", "Tech Support")
user_repository.save(user7)

product1 = Product("GeniusPDF")
product_repository.save(product1)

product2 = Product("Diamond Scan")
product_repository.save(product2)

product3 = Product("docuMental")
product_repository.save(product3)

product4 = Product("OmniConverter")
product_repository.save(product4)

pdb.set_trace()