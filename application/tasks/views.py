from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.tasks.models import Task
from application.tasks.forms import TaskForm

from application.groups.models import Group
from flask_login import current_user


@app.route("/tasks", methods=["GET"])
def tasks_index():
    groups = Group.query.all()
    print("GROUPSUOUOUOUO{}".format(groups))
    print("GROUPIN     NIMET {}".format([group.name for group in groups]))
    return render_template("tasks/list.html", tasks = Task.query.all(),
                                              groups = Group.query.all())

@app.route("/tasks/new/")
@login_required(role="ADMIN")
def tasks_form():
    return render_template("tasks/new.html", form = TaskForm())

@app.route("/delete/<task_id>/", methods=["POST"])
@login_required(role="ADMIN")
def task_delete(task_id):
    t = Task.query.get(task_id)
    if t.account_id != current_user.id:
        return login_manager.unauthorized()
    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("tasks_index"))

@app.route("/tasks/<task_id>/", methods=["POST"])
@login_required(role="ADMIN")
def tasks_set_done(task_id):
    t = Task.query.get(task_id)
    if t.account_id != current_user.id:
        return login_manager.unauthorized()
    if t.done == True:
        t.done = False
    else:
        t.done = True
    #t.done = True
    db.session().commit()

    return redirect(url_for("tasks_index"))

@app.route("/tasks/", methods=["POST"])
@login_required(role="ADMIN")
def tasks_create():
    form = TaskForm(request.form)

    # if not form.validate():
    #     print("NONONONONONO")
    #     return render_template("tasks/new.html", form = form)

    print("FORMROMORMROMROMROMRORM {}".format(form))
    t = Task(form.name.data)
    t.done = form.done.data
    t.account_id = current_user.id
    t.group_id = form.groups.data


    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tasks_index"))
