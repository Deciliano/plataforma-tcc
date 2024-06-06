#! /usr/bin/env python3

from flask import Flask
from config import Config
from db import init_db
from productController import product_bp

app = Flask(__name__)
app.config.from_object(Config)

init_db(app)

app.register_blueprint(product_bp)

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')
