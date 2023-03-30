import flask
import website

bp = flask.Blueprint("blog", __name__, url_prefix="/blog")


@bp.route("/")
def blog():
    pass


@bp.route("/<int:id>")
def post():
    pass
