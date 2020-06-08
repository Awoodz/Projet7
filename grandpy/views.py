from flask import Flask, render_template, request, jsonify
import grandpy.grandpy as gp


app = Flask(__name__)

app.config.from_object('config')

@app.route("/")
def index():
    return render_template('P7.html')

@app.route("/userinput", methods=["POST"])
def userinput():
    user_input = request.form["form_input"]
    response = gp.traitement(user_input)
    print(jsonify(response))
    return jsonify(response)
