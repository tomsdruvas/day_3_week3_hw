from app import app
from flask import render_template
from models.orders import list_of_orders



@app.route('/')
def index():
    return render_template('index.html', title = "Orders", list_of_orders = list_of_orders)


@app.route('/order/<index>')
def order():
    return render_template('order.html', title = "Order by ID", list_of_orders = list_of_orders)

