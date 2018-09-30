import sys

from flask import Flask, render_template, request,json

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

# def hello():
#     return "Welcome to Python Flask!"

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
    
@app.route("/signup")
def signUp():
    return render_template("signUp.html")

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username']
    password = request.form['password']
    return json.dumps({'status':'OK','user':user,'pass':password})

if __name__ == "__main__":
    app.run()
