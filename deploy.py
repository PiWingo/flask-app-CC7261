from flask import Flask, request
import threading
import time

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def postData():

    data = request.get_json()

    for x in data:
        print(x)

    return data



def create_app():
    global app
    return app
