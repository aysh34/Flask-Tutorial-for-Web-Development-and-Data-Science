from flask import Flask, request, redirect, url_for, Response

app = Flask(__name__)


'''
Core Objects ---> what they do

request --> read what the user sends 
redirect --> move the user to different page
Response --> send something back to user
url_for() --> build the route dynamically from function name
session --> remember one user information across the pages

'''
@app.route('/')
def home():
    pass

if __name__ == '__main__':
    app.run(debug=True)