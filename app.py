from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world!"

__name__ == "__main__" 

from equipamento_controller import *