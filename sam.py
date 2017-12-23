from flask import Flask, request, redirect, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to the webpage"

@app.route('/code', methods=['POST'])
def code():
    email = request.form['email']
    password = request.form['password']
    return "hii"



if __name__ == '__main__':
    app.run(debug=True)