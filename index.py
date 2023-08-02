from flask import Flask
from router import allRoute
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)
app.register_blueprint(allRoute, url_prefix="/api")

if __name__ == '__main__':
    app.run(debug=True , host= '0.0.0.0' , port='3000')

