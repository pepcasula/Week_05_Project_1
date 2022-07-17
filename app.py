from flask import Flask, render_template

from controllers.ticket_controller import tickets_blueprint
from controllers.bug_controller import bugs_blueprint
from controllers.product_controller import products_blueprint
from controllers.user_controller import users_blueprint

app = Flask(__name__)

app.register_blueprint(tickets_blueprint)
app.register_blueprint(bugs_blueprint)
app.register_blueprint(products_blueprint)
app.register_blueprint(users_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)