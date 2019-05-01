"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    projects_grades = hackbright.get_grades_by_github(github)

    print(projects_grades)

    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github,
                            projects_grades=projects_grades)
    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/add_student")
def get_student_add_form():
    """Show form for adding a student."""

    return render_template("new_student.html")

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add student."""

    #first_name, last_name, github = request.form.get('first_name, last_name, github')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)

    return render_template("student-added.html",
                           first_name=first_name,
                           last_name=last_name,
                           github=github)


@app.route("/project", methods=['GET'])
def get_project_info():
    """Show information about a project."""

    project_title = request.args.get('title')

    title, description, max_grade = hackbright.get_project_by_title(project_title)

    return render_template("project_info.html",
                           title=title,
                           description=description,
                           max_grade=max_grade)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
