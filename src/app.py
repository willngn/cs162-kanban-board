import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Kanban(db.Model):
    id = db.Column('task_id', db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(500))
    status = db.Column(db.String(50))

    def __repr__(self):
        return f'<Task {self.id}: {self.title}>'
@app.route("/")
def index():
    todo = Kanban.query.filter_by(status='todo').all()
    doing = Kanban.query.filter_by(status='doing').all()
    done = Kanban.query.filter_by(status='done').all()
    return render_template('index.html', todo=todo, doing=doing, done=done)

# because we add more tasks to the board --> add data 
# --> we need to post to server
@app.route('/add-task', methods = ['POST'])
def add_task():
    holder = Kanban(title=request.form['title'], description=request.form['description'], status=request.form['status'])
    db.session.add(holder)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update-status/<task_id>/<task_status>', methods = ['POST'])
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
    db.create_all()
    app.run(debug=True, port=5000)