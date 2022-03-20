from flask import Flask, render_template, request
app = Flask(__name__)

# saving data by making it global
products = ["Pen", "Pencil", "Eraser"]
cart_items = []


@app.route("/")
def index():
    return render_template("index.html", cart_items=cart_items)


@app.route("/products")
def show_products():
    return render_template("products.html", products=products)


@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    name = request.form['name']
    cart_items.append(name)
    return render_template("index.html", cart_items=cart_items)
