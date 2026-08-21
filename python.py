from flask import Flask, render_template, request, redirect

app = Flask(__name__)

products = [
    {"id": 1, "name": "Black T-Shirt", "price": 799},
    {"id": 2, "name": "Denim Jacket", "price": 1499},
    {"id": 3, "name": "Summer Dress", "price": 1299},
    {"id": 4, "name": "White Sneakers", "price": 1799},
    {"id": 5, "name": "Casual Hoodie", "price": 1199},
    {"id": 6, "name": "Fashion Handbag", "price": 999}
]

cart = []


@app.route("/")
def home():
    total = sum(item["price"] for item in cart)

    return render_template(
        "index.html",
        products=products,
        cart=cart,
        total=total
    )


@app.route("/add/<int:product_id>")
def add_to_cart(product_id):

    for product in products:
        if product["id"] == product_id:
            cart.append(product)

    return redirect("/")


@app.route("/clear")
def clear_cart():
    cart.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)