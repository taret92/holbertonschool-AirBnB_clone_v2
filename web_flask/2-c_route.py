#!/usr/bin/python3
"""FLASK MODULES"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_route():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb_route():
    return "HBNB"


@app.route("/c/<text>")
def c_route(text):
    text = text.replace("_", " ")
    return "C " + text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
