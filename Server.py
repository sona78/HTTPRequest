import flask
from flask import Flask, request, Response, jsonify, abort
import os

app = flask.Flask(__name__)


@app.route("/", methods=["GET","POST"])

def main():
    data = {"data":"No Data Entered","success": False}

    params = flask.request.json
    if (params == None):
        params = flask.request.args

    if (params != None):
        data["Data"] = params.get("data")
        data["ValueEntered"] = True

    return flask.jsonify(data)


app.run(host='0.0.0.0')

# 1. in cmd, cd appsetup
# 2. in cmd, cd scripts
# 3. in cmd, activate
# 4. in cmd, cd ..
# 5. in cmd, cd ..
# 6. in cmd, pip install -r requirements.txt
# 7. in cmd, set FLASK_APP=Server.py
# 8. in cmd, flask run