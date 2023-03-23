import flask
import website

bp = flask.Blueprint("projects", __name__, url_prefix="/projects")


@bp.route("/")
def projects():
    db = website.db.get_db()
    projects = db.execute("SELECT * FROM project").fetchall()

    if projects is None:
        flask.abort(404, "Could not find projects")

    return flask.render_template("projects/index.html", projects=projects)


@bp.route("/<int:id>")
def project(id):
    db = website.db.get_db()
    project = db.execute("SELECT * FROM project WHERE project.id = ?",
                         (id,)).fetchone()

    if project is None:
        flask.abort(404, f"Project {id} does not exist")

    return flask.render_template("projects/project.html", project=project)
