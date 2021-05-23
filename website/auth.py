# from typing_extensions import ParamSpec
from website import create_app
from flask import Blueprint, render_template, request, flash, redirect, url_for

auth = Blueprint('auth', __name__)


@auth.route('/signUp', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 4:
            flash('Email should have at least 4 characters', category="Error")
        elif len(firstName) < 1:
            flash('First Name should have at least 1 character', category="Error")
        elif len(password1) < 7:
            flash('Password should have at least 8 characters', category="Error")
        elif password1 != password2:
            flash('Your password donot match.', category="Error")
        else:
            # update database
            flash('Account Created!', category="Success")

    return render_template("signup.html")


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return '<p>Working</p>'
