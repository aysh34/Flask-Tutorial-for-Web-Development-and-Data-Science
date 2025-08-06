from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        age = request.form.get("age")
        return redirect(
            url_for("your_info", username=username, password=password, age=age)
        )
    return render_template("index.html")


@app.route("/your_info")
def your_info():
    username = request.args.get("username")
    password = request.args.get("password")
    age = request.args.get("age")
    return render_template(
        "your_information.html", username=username, password=password, age=age
    )


if __name__ == "__main__":
    app.run(debug=True)
