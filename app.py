#! /usr/bin/env python3

from flask import Flask
from storage.db import init_db
from config import Config

from controllers.clientController import client_bp

app = Flask(__name__)
app.config.from_object(Config)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

app.register_blueprint(client_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')