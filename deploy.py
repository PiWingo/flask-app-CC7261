from flask import Flask, request
import threading
import time
import json

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def postData():

    data = json.loads(request.get_json())
    print(data)

    return data



def create_app():
    global app
    return app
