from flask import Blueprint, render_template

auths = Blueprint('auths', __name__)

@auths.route('/login')
def login():
    return render_template("login.html")

@auths.route('/logout')
def logout():
    return render_template("login.html")

@auths.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")