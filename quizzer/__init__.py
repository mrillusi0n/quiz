from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '802394YHFRIUAOERY5T0287345'

from . import routes