from flask import Flask, request
import threading
import time

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def postData():

    x = request.data

    print(x)

    return x



def create_app():
    global app
    return app
