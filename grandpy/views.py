from flask import Flask, render_template, request, jsonify
import grandpy.app as app


app_flask = Flask(__name__)

app_flask.config.from_object('config')

@app_flask.route("/")
def index():
    return render_template('index.html')

@app_flask.route("/userinput", methods=["POST"])
def userinput():
    user_input = request.form["form_input"]
    response = app.get_request(user_input)
    return jsonify(response)
