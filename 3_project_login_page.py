# let's create a basic login page
"""
1. Show the login page
2. Accept username & password from the user
3. Store user info in session
4. Redirect to the welcome page
5. Logout

"""

from flask import Flask, request, redirect, url_for, Response, session

app = Flask(__name__)
app.secret_key = "9211"  # required if you're working with sessions -- LOCK the SESSION

"""
Core Objects ---> what they do

request --> read what the user sends 
redirect --> move the user to different page
Response --> send something back to user
url_for() --> build the route dynamically from function name
session --> remember the user information(username/id etc) across the pages

"""


@app.route("/", methods=["GET", "POST"])  # user will see as well as post some info
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session["user"] = (
                username  # store the username in session --> session['user'] = 'Ayesha'
            )

            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials", mimetype="text/plain")
    return """
        <h2> Login Page </h2>
        <form method='POST'>
        <label>Username: <input type="text" name="username"></label><br><br>
        <label>Password: <input type="password" name="password"></label><br><br>  
        <input type='submit' value='Login'>   
        </form> 
        """


@app.route("/welcome")
def welcome():
    if "user" in session:
        return f"""
        <h2> Welcome, {session["user"]}!</h2>
        <a href={url_for('logout')}>Logout</a>
        """
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove the user key from the session
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
