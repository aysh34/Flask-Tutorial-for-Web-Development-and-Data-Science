# Create a Flask app with two routes: /hello (returns "Hello, World!") and /about (returns your short bio).

from flask import Flask, render_template, request, redirect, Response, url_for, flash

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/about")
def about():
    return "Hi 👋 I'm Ayesha Saleem"


if __name__ == "__main__":
    app.run(debug=True)
