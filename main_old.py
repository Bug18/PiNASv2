#NAS Web API

from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from hashing_alg_v2 import hashing_func, check_passwd
import sys
import os


app = Flask(__name__)
app.secret_key = "12345"
app.permanent_session_lifetime = timedelta(hours=24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

database = SQLAlchemy(app)


class Users(database.Model):
    _id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100))
    email = database.Column(database.String(100))
    passwd = database.Column(database.String(200))

    def __init__(self, name, email, passwd):
        self.name = name
        self.email = email
        self.passwd = passwd






@app.route("/")
def home_page():
    if "user" in session:
        user = session["user"]
        return render_template("home.html", content=f"Welcome {user}")
    else:
        return render_template("home.html")

@app.route("/files", methods=["POST", "GET"])
def files():
    if "user" in session:
        user = session["user"]
        if "email" in session:
            email = session["email"]
            return render_template("files.html", user=user, email=email)
    else:
        flash("Not logged in! Please login first!", "info")
        return redirect(url_for("login"))
    return render_template("files.html", user=user)


@app.route("/admin")
def admin():

    return render_template("admin.html")



@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        passwd = request.form["passwd"]

        #found_user = users.query.filter_by(name=user).first()
        #found_passwd = users.query.filter_by().first()
        """
        if found_user:
            flag = check_passwd(passwd, found_passwd)
            if flag == True:
                passwd = None"""
        session["user"] = user
        flash("Login successfull! You are now logged in!")
        return redirect(url_for("files"))
            #else:
                #flash("Incorrect password!")
    else:
        if "user" in session:
            flash("Already logged in!", "info")
            return redirect(url_for("files"))

    return render_template("login.html")



@app.route("/logout")
def logout():
    try:
        user = session["user"]
        session.pop("user", None)
        flash("Logged out succsessfully!", "info")
    except:
        flash("Please login first!", "info")
    return redirect(url_for("login"))











if __name__ == "__main__":
    database.create_all()
    app.run(debug=True)
