from src import create_app
from flask_sqlalchemy import SQLAlchemy

app = create_app()
db = SQLAlchemy(app)
class Kanban(db.Model):
    __tablename__ = "kanban"
    id = db.Column('task_id', db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(500))
    status = db.Column(db.String(50))

    def __repr__(self):
        return f'<Task {self.id}: {self.title}>'

db.create_all()
db.session.commit()