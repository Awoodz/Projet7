from flask import Flask, render_template, request, jsonify
import grandpy.grandpy as gp


app = Flask(__name__)

app.config.from_object('config')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/userinput", methods=["POST"])
def userinput():
    user_input = request.form["form_input"]
    response = gp.get_request(user_input)
    return jsonify(response)
