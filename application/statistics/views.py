from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.auth.models import User

@app.route("/statistics", methods=["GET"])
def statistics_index():
    return render_template("statistics/list.html", users_list = User.query.all())
