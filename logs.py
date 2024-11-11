from flask import Flask
from src.logger import logging

app = Flask(__name__)


@app.route('/', methods = ["GET", "POST"])
def index():
    logging.info("TEST FILE.")

    return "Welcome to my first ML PROJECT TEST"

if __name__ == "__main__":
    app.run(debug= True)  # default port no = 5000
