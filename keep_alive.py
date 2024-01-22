from flask import Flask
from threading import Thread
import random
import time
import requests
import logging

app = Flask(__name__)

@app.route("/")
def home():
    return "You have found the home of a Python program!"

def run():
    app.run(host="0.0.0.0", port=random.randint(2000, 9000))

def ping(target, debug):
    while True:
        r = requests.get(target)
        if debug:
            print(r.status_code)
        time.sleep(random.randint(30, 60))

def awake(target, debug=False):
    log = logging.getLogger("werkzeug")
    log.disabled = True
    app.logger.disabled = True
    t = Thread(target=run)
    r = Thread(target=ping, args=(target, debug))
    t.start()
    r.start()

if __name__ == "__main__":
    awake("http://localhost:5000", debug=False)