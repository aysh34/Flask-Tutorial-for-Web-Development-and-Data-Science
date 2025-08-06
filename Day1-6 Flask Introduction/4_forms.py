from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/welcome",methods=['POST'])
def welcome():
    username = request.form.get("username")
    password = request.form.get("password")

    user_pass = {"ayesha": "123", "iqra": "456"}
    if username in user_pass and user_pass[username] == password:
        return render_template("welcome.html")
    else:
        return "Wrong credentials"


if __name__ == "__main__":
    app.run(debug=True)
