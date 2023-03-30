import flask
import website

bp = flask.Blueprint("blog", __name__, url_prefix="/blog")


@bp.route("/")
def blog():
    db = website.db.get_db()
    blog = db.execute("SELECT * FROM blog").fetchall()

    if blog is None:
        flask.abort(404, "could not find blog")

    return flask.render_template("blog/index.html", blog=blog)


@bp.route("/<int:id>")
def post():
    db = website.db.get_db()
    post = db.execute("SELECT * FROM blog WHERE blog.id = ?",
                      (id,)).fetchone()

    if post is None:
        flask.abort(404, f"post {id} does not exist")

    return flask.render_template("blog/post.html")
