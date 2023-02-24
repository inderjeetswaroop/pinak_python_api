from flask import Flask
application = Flask(__name__)

@applications.route('/')
def hello_world():
    return "Hello Inder"