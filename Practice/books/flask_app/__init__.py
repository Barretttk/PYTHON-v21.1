from msilib import schema
from flask import Flask

app = Flask(__name__)

#================================
# Whats the data base - ie schema
#================================
DATABASE = "books_schema"

app.secret_key = "ofghsgogdoigsdikn"