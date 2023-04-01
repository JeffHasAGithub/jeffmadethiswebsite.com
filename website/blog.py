import flask
import website

bp = flask.Blueprint("blog", __name__)


@bp.route("/")
def index():
    db = website.db.get_db()
    posts = db.execute("SELECT * FROM post").fetchall()

    if posts is None:
        flask.abort(404, "could not find blog")

    return flask.render_template("blog/index.html", posts=posts)


@bp.route("/<int:id>")
def post(id):
    db = website.db.get_db()
    post = db.execute("SELECT * FROM post WHERE post.id = ?",
                      (id,)).fetchone()

    if post is None:
        flask.abort(404, f"post {id} does not exist")

    return flask.render_template("blog/post.html")
