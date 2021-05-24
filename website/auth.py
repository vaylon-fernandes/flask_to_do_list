# from typing_extensions import ParamSpec
from website import create_app
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required

auth = Blueprint('auth', __name__)


@auth.route('/signUp', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()

        if user:
            flash('Account already exists')
            return redirect(url_for("views.login"))
        elif len(email) < 4:
            flash('Email should have at least 4 characters', category="Error")
        elif len(firstName) < 1:
            flash('First Name should have at least 1 character', category="Error")
        elif len(password1) < 8:
            flash('Password should have at least 8 characters', category="Error")
        elif password1 != password2:
            flash('Your password donot match.', category="Error")
        else:
            # update database
            new_user = User(email=email, first_name=firstName,
                            password=generate_password_hash(password1, 'sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)

            flash('Account Created!', category="Success")
            return redirect(url_for("views.to_do_list"))

    return render_template("signup.html", user=current_user)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in sucessfully", category="Success")
                login_user(user, remember=True)
                return redirect(url_for('views.to_do_list'))
            else:
                flash('Incorrect Password, Please try again', category="Error")
        else:
            flash('Please Create a account first', category="Error")
            return redirect(url_for("auth.sign_up"))

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
