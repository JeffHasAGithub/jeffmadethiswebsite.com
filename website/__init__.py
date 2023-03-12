import os
from flask import Flask, render_template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
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

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/projects")
    def projects():
        return render_template("projects.html")

    @app.route("/resume")
    def resume():
        return render_template("resume.html")

    return app
