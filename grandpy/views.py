from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('P7.html')


@app.route('/', methods=['POST'])
def get_form_input():
    user_input = request.form['form_input']
    print(user_input)
    return render_template('P7.html')


app.config.from_object('config')
