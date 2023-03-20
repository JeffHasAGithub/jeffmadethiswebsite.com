from flask import Blueprint, render_template

bp = Blueprint("projects", __name__)


@bp.route("/projects")
def projects():
    return render_template("projects.html")
