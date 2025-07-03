from flask import Flask, render_template, request, redirect

'''
request --> read whatever the user has send
redirect --> move the user to a different page within the website
GET (requesting data), POST (sending data).
'''

app = Flask(__name__)


@app.route("/")
def home():
    return 'Home'

# HTTP METHODS ====> GET, POST  =====================================

@app.route("/about", methods=["GET", "POST"]) # by-default method is "GET"
def about():
    if request.method == "GET": # You're getting/viewing some data/info from server or simply visiting a URL
        return "GET Method" 
    else:
        return "POST Method" # You're sending info/data to server for processing


if __name__ == "__main__":
    app.run(debug=True)
