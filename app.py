from flask import Flask
import pandas as pd
import numpy as np


app = Flask(__name__)


@app.route('/', methods=['GET', "POST"])
def home():
    text = "This is Flask front end page with docker"
    return text


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
