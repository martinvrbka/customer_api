from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from database import db
import os

app = Flask(__name__)
api = Api(app)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
db.init_app(app)

if __name__ == '__main__':
    app.run(port=3333, debug=True)