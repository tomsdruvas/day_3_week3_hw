from app import app
from flask import render_template
from models.orders import list_of_orders



@app.route('/')
def index():
    return render_template('index.html', title = "Orders", list_of_orders = list_of_orders)


@app.route('/order/<int:order_id>')
def order(order_id):
    order_id -= 1
    return render_template('order.html', order_num = order_id +1, order = list_of_orders[order_id])

