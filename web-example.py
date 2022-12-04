#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route("/inst/dmm/fetch.json")
def inst_dmm_fetch():
    return {"fetch":0.01}

@app.route("/")
def hello_world():
    return " <link rel=\"stylesheet\" type=\"text/css\" href=\"/static/content/styles/main.css\" /><p class=\"red\" >Hello, World!</p>"

