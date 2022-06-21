from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from router import allRoute
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = config['DB']['ORM']
app.config['JSON_SORT_KEYS'] = False
app.register_blueprint(allRoute, url_prefix="/")
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True , host= '0.0.0.0' , port='3000')

