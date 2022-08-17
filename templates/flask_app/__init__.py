from flask import Flask
from flask_bcrypt import Bcrypt



app = Flask(__name__)


app.secret_key = "ofghsgogdoigsdikn"

#================================
# Whats the data base - ie schema
#================================


DATABASE = "login_schema"

bcrypt = Bcrypt(app)