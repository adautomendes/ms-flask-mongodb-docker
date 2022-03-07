from flask import Flask, jsonify, make_response
from model.weapon import Weapon

app = Flask(__name__)

@app.route("/")
def hello_world():
  return make_response(jsonify(Weapon("Ak47", 123, 456).__dict__), 200)