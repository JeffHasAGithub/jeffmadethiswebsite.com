import os
import werkzeug
from flask import Flask, render_template

from website.db import get_db


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    setup_config(app, test_config)
    setup_routes(app)
    setup_database(app)

    from . import projects
    app.register_blueprint(projects.bp)

    return app


def setup_config(app, test_config):
    app.config.from_mapping(
        KEY="dev",
        DB=os.path.join(app.instance_path, "website.sqlite"),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


def setup_routes(app):
    @app.errorhandler(werkzeug.exceptions.HTTPException)
    def error(err):
        return render_template("error.html", err=err), err.code

    @app.route("/")
    def index():
        db = get_db()
        projects = db.execute("SELECT * FROM project").fetchall()

        return render_template("index.html", projects=projects)

    @app.route("/resume")
    def resume():
        return render_template("resume.html")


def setup_database(app):
    from . import db
    db.register_db(app)
