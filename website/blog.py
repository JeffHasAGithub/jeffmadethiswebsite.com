import flask
import website

bp = flask.Blueprint("blog", __name__, url_prefix="/blog")
