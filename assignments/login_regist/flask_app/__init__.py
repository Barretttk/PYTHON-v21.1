from flask import Flask

app = Flask(__name__)

#================================
# Whats the data base - ie schema
#================================
DATABASE = "login_schema"

app.secret_key = "ofghsgogdoigsdikn"