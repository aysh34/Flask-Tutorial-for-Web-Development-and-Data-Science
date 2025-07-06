"""
Template inheritance in Jinja is a powerful feature that helps you avoid duplication, organize your code, and promote reusability in web applications

base.html → defines the skeleton

home.html, about.html, etc. → inherit from base.html and fill in specific content


"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
