from flask import Blueprint, render_template, request, redirect, flash, jsonify, url_for
from flask_login import login_required, current_user
from .models import ToDoList
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['POST', 'GET'])
@login_required
def to_do_list():
    request_is_post = request.method == "POST"
    if request_is_post:
        task_content = request.form["content"]
        new_task = ToDoList(task=task_content, user_id=current_user.id)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for("views.to_do_list"))
        except:
            db.session.rollback()
            return 'There was an issue adding your task'
    else:
        datecreated = ToDoList.date_created
        tasks = ToDoList.query.order_by(datecreated).all()
        return render_template("index.html", tasks=tasks, user=current_user)


@views.route('/delete/<int:task_id>', methods=['GET', 'POST'])
@login_required
def delete(task_id):
    task_to_delete = ToDoList.query.get_or_404(task_id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect(url_for("views.to_do_list"))
    except:
        db.session.rollback()
        return 'Deletion Failed'


@views.route('/deleteAll', methods=['GET', 'POST'])
@login_required
def delete_all():
    try:
        db.session.query(ToDoList).delete()
        db.session.commit()
        return redirect(url_for("views.to_do_list"))
    except:
        db.session.rollback()
        return 'Could not delete'


@views.route('/update/<int:task_id>', methods=['GET', 'POST'])
@login_required
def update(task_id):
    task_to_update = ToDoList.query.get_or_404(task_id)
    request_is_post = request.method == "POST"
    if request_is_post:
        task_to_update.task = request.form['update']
        try:
            db.session.commit()
            return redirect(url_for("views.to_do_list"))
        except:
            db.session.rollback()
            return 'Updation Failed'
    else:
        return render_template('update.html', task=task_to_update)
