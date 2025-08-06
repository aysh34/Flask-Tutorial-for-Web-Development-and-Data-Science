# Dynamic URL Routing: Create a route /user/<username> that displays a welcome message with the username.

from flask import Flask, render_template, request, redirect, Response, url_for, flash

app = Flask(__name__)


@app.route("/user/<username>")
def home(username):
    return f"Welcome, {username}!"


if __name__ == "__main__":
    app.run(debug=True)
