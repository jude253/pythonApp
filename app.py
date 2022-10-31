from flask import Flask

api = Flask(__name__)

@api.route('/')
def home():
    response_body = {
        "message" :"Hello World!"
    }

    return response_body