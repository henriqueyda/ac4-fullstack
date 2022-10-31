from flask import Flask
from models.product import Product


app = Flask(__name__)

@app.route('/v1/product/', methods=["GET"])
def index():
    return Product.json_return()


@app.route('/v1/product/total', methods=["GET"])
def total_price():
    return Product.total_price()

if __name__ == '__main__':
    app.run(debug=True,port= 5000)