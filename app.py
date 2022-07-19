from flask import Flask, render_template

from controllers.ticket_controller import tickets_blueprint
from controllers.bug_controller import bugs_blueprint
from controllers.product_controller import products_blueprint
from controllers.user_controller import users_blueprint
import repositories.product_repository as product_repository



app = Flask(__name__)

app.register_blueprint(tickets_blueprint)
app.register_blueprint(bugs_blueprint)
app.register_blueprint(products_blueprint)
app.register_blueprint(users_blueprint)

@app.route('/')
def home():
    all_products = product_repository.select_all()
    return render_template('index.html', all_products = all_products)

if __name__ == '__main__':
    app.run(debug=True)