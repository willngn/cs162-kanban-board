from src import db, app
from flask import render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from .models import Kanban

@app.route("/")
def index():
    todo = Kanban.query.filter_by(status='todo').all()
    doing = Kanban.query.filter_by(status='doing').all()
    done = Kanban.query.filter_by(status='done').all()
    return render_template('index.html', todo=todo, doing=doing, done=done)
    
# because we add more tasks to the board --> add data 
# --> we need to post to server
@app.route('/add_task', methods = ['POST'])
def add_task():
    holder = Kanban(title=request.form['title'], description=request.form['description'], status=request.form['status'])
    db.session.add(holder)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update_status/<task_id>/<task_status>', methods = ['POST'])
def update_status(task_id, task_status):
    holder = Kanban.query.filter_by(id=task_id).first()
    holder.status = task_status
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<task_id>', methods=['POST'])
def delete(task_id):
    Kanban.query.filter_by(id=task_id).delete()
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)