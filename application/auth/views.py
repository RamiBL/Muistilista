from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, NewUserForm




@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

    login_user(user)
    print("Käyttäjä " + user.name + " tunnistettiin")
    return redirect(url_for("index"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/new/")
def new_user_form():
    return render_template("auth/new.html", form = NewUserForm())


@app.route("/auth/", methods=["POST"])
def users_create():
    form = NewUserForm(request.form)

    if not form.validate():
        return render_template("auth/new.html", form = form)

    username = form.username.data
    if User.query.filter_by(username=username).first() is None:
        print("BLÖÖÖÖÖÖÖÖÖÖ {}".format(username))
        print("BLÄÄÄÄÄÄÄÄÄÄÄÄ {}".format(form.password.data))
        user = User(username, form.password.data)
    else:
        return render_template("auth/new.html", form = NewUserForm())

    db.session().add(user)
    db.session().commit()

    return redirect(url_for("auth_login"))
