# Passing Query Parameters
# Use /square?num=5 to return the square of the number passed via the query string.

"""
Query parameters are the key=value pairs you pass in a URL after a ?
In Flask, request.args is an ImmutableMultiDict object that allows access to the parsed contents of the query string in a GET request. The query string is the part of the URL after the question mark (e.g., ?key1=value1&key2=value2).

Example:
/square?num=5

Here:

/square is the route
?num=5 is the query string
num is the query parameter

"""
from flask import Flask, render_template, request, redirect, Response, url_for, flash

app = Flask(__name__)


@app.route("/square")
def home():
    num = request.args.get("num", type=int)
    if num is None:
        return Response("Missing parameter", status=400)
    return str(num**2)


if __name__ == "__main__":
    app.run(debug=True)
