from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

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
