from flask import Blueprint, render_template, abort
from website.db import get_db

bp = Blueprint("projects", __name__, url_prefix="/projects")


@bp.route("/")
def projects():
    return render_template("projects/index.html")


@bp.route("/<int:id>")
def project(id):
    db = get_db()
    project = db.execute("SELECT * FROM project"
                         " WHERE project.id = ?").fetchone()

    if project is None:
        abort(404, f"Project {id} does not exist")

    return render_template("project.html")
