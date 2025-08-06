"""
Flash messages are a way to provide feedback to users in a web application. They can be used to inform users about the success or failure of an action, such as submitting a form or saving data. In this example, we will create a simple Flask application that uses flash messages to notify users about the status of their actions.
"""

from flask import Flask, redirect, render_template, flash, url_for, request

app = Flask(__name__)
app.secret_key = "123"


@app.route("/")
def index():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        name = request.form.get("username")
        if not name:
            flash("Please enter your name")
            return render_template("form.html")
        else:
            flash("Successfully done!")
            return redirect(url_for("thankyou"))
    return redirect(url_for("index"))


@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")


if __name__ == "__main__":
    app.run(debug=True)
