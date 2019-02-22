from application import app, db
from flask import redirect, render_template, request, url_for
from application.groups.models import Groups
from application.groups.forms import GroupsForm
from flask_login import login_required, current_user

@app.route("/group/<group_id>/", methods=["POST"])


@app.route("/groups", methods=["GET"])
def groups_index():
    return render_template("groups/list.html", groups = Groups.query.all())

@app.route("/groups/new/")
@login_required
def groups_form():
    return render_template("groups/new.html", form = GroupsForm())

@app.route("/groups/", methods=["POST"])
@login_required
def groups_create():
    form = GroupsForm(request.form)

    if not form.validate():
        return render_template("groups/new.html", form = form)

    t = Groups(form.name.data)


    db.session().add(t)
    db.session().commit()

    return redirect(url_for("groups_index"))
