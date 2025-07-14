# Simple HTML Template Rendering
# Create a /greet/<name> route that renders a template and displays: "Good to see you, <name>!"

from flask import Flask, render_template, request, redirect, Response, url_for, flash

app = Flask(__name__)


@app.route("/greet/<name>")
def greet(name):
    return render_template("home.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
