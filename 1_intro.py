from flask import Flask

# Create a Flask application instance.
# __name__ refers to the name of the current Python module.
# Flask uses it to locate resources like templates and static files.
app = Flask(__name__)


# Define a route decorator. This maps URLs to Python functions.
# When a user navigates to the root URL ('/'), this function will be executed.
@app.route("/")
def hello_world():
    # This function returns the string "Hello, World!".
    # Flask automatically sends this string as an HTTP response with a 200 OK status.
    return "Hello, World!"


# This block ensures that the development server only runs when the script is executed directly.
# It prevents the server from running if the script is imported as a module into another script.
if __name__ == "__main__":
    # Run the Flask development server.
    # debug=True enables debug mode, which provides helpful error messages
    # and automatically reloads the server on code changes.
    app.run(debug=True)
