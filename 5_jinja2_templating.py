"""

jinja2 templating -- it's a templating engine in flask that helps you to create dynamic html pages. You can implement the python code/logic (variables,loops,conditions) within the html template/code
It basically helps your python backend server to talk to your frontend html.

----Syntax-----

variables -- {{variable_name}}
conditions -- {% if condition %} .... {% endif %}
for loop -- {% for item in list%} .... {% endfor %}

"""

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def home():
    student_report = {
        "name": "Ayesha",
        "marks": 675,
        "skills": ["Data Science", "Maths", "ML"],
    }
    return render_template("report.html", **student_report)


if __name__ == "__main__":
    app.run(debug=True)
