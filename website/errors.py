from flask import Blueprint, render_template

bp = Blueprint("errors", __name__)


@bp.app_errorhandler(404)
def page_not_found(err):
    return render_template("errors/404.html", err=err)
