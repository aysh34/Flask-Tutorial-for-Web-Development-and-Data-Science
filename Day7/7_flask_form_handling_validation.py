"""
1. Manual form handling:
There is a feedback form on your website -> Users fill up(input) and submit that form -> Now you want flask to receive and process that input/data -> and redirect the user to a thank you page

2. Flash messages -> are a way to show one-time notifications in web applications—typically for alerts like "Login successful", "Error uploading file", or "Item deleted". In Flask, they are commonly used to communicate the result of a user action.
- Flask uses the session to store flash messages, so you need a secret key.
flash(message, category)


"""

from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = "123"


@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":  # check whether the form is submitted?
        name = request.form.get(
            "username"
        )  # request.form['key'] but through error if key not exist
        if not name:
            flash("Name cannot be empty", "error")
            return redirect(url_for("form"))
        message = request.form.get("message")
        flash(f"Thank you {name}! your feedback is saved", "success")
        return redirect(url_for("thankyou", name=name, message=message))

    return render_template("feedback.html")


@app.route("/thankyou")
def thankyou():
    name = request.args.get("name")
    message = request.args.get("message")
    return render_template("thankyou.html", name=name, message=message)


if __name__ == "__main__":
    app.run(debug=True)
