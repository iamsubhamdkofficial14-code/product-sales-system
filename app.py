from flask import Flask, render_template, request, redirect

app = Flask(__name__)

products = [
    {"id": "P001", "name": "Laptop", "quantity": 25, "price": 60000},
    {"id": "P002", "name": "Desktop", "quantity": 65, "price": 23000},
    {"id": "P003", "name": "Monitor", "quantity": 44, "price": 10000},
    {"id": "P004", "name": "Mouse", "quantity": 21, "price": 800},
    {"id": "P005", "name": "Headphone", "quantity": 43, "price": 1200},
    {"id": "P006", "name": "CPU", "quantity": 45, "price": 30000},
    {"id": "P007", "name": "Earbuds", "quantity": 20, "price": 700},
    {"id": "P008", "name": "Mobile", "quantity": 50, "price": 25000}
]


@app.route("/")
def home():

    total_sales = 0

    for product in products:
        product["total"] = product["quantity"] * product["price"]
        total_sales += product["total"]

    return render_template(
        "index.html",
        products=products,
        total_sales=total_sales
    )


@app.route("/add", methods=["POST"])
def add_product():

    product_id = request.form["id"]
    name = request.form["name"]
    quantity = int(request.form["quantity"])
    price = int(request.form["price"])

    products.append({
        "id": product_id,
        "name": name,
        "quantity": quantity,
        "price": price
    })

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)