import sys
from flask import Flask
from datetime import datetime
import re
from flask import render_template


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

@app.route("/hello/<name>")
def hello_there(name):
    #now = datetime.now()
    #formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expression. URL arguments
    # can contain arbitary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)
    
    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"
    
    # BAD CODE! Avoid inline HTML for security reason, plus templates automatically escape HTML content.
    # content = "Hello there, " + clean_name + "! it's " +  formatted_now
    #content = "<strong>Hello there, " + name + "!</strong> It's " + {{ date.strftime("%A, %d %B, %Y at %X") }}.
    
    # return content
    #return render_template("hello_there.html",title="Hello, Flask",content=content)
    return render_template(
        "hello_there.html",
        name=clean_name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

if __name__ == "__main__":
    app.run()