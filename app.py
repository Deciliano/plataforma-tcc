#! /usr/bin/env python3

from flask import Flask
from storage.db import db, create_tables

from controllers.clientController import client_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    create_tables()

app.register_blueprint(client_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')