import src
from src.models import Kanban
from src import app, db
import unittest
import tempfile

class appFunctionalityTesting(unittest.TestCase):
    def setUp(self):
        self.db_test, app.config["DATABASE"] = tempfile.mkstemp()
        src.testing = True
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self) -> None:
        return super().tearDown()

    def add(self, title, des, status):
        """ request: generally add a task - any status """
        return self.app.post('/add_task', data=dict(title=title,
                                               description=des,
                                               status=status),
                                     follow_redirects=True)

    def update(self, id, new_status):
        """ request: generally move a task around - any status """
        return self.app.post('/update_status/' + str(id) + '/' + str(new_status),
                          data=dict(id=id, status=new_status),
                          follow_redirects=True)

    def delete(self, id):
        """ request: generally delete any task """
        return self.app.post('/delete/' + str(id), data=dict(id=id), follow_redirects=True)
    
    def testAddTasks(self):
        """ When added, a task should exist at its right category """
        # todo
        self.add(title="Hello", des="Hey", status="todo")
        holder1 = db.session.query(Kanban).filter(Kanban.title=='Hello').first()
        self.assertEqual(holder1.description, 'Hey')
        self.assertEqual(holder1.status, 'todo')

        # doing
        self.add(title="Hi", des="Hola", status="doing")
        holder2 = db.session.query(Kanban).filter(Kanban.title=='Hi').first()
        self.assertEqual(holder2.description, 'Hola')
        self.assertEqual(holder2.status, 'doing')

        # done
        self.add(title="Heeyy", des="Helloo", status="done")
        holder3 = db.session.query(Kanban).filter(Kanban.title=='Heeyy').first()
        self.assertEqual(holder3.description, 'Helloo')
        self.assertEqual(holder3.status, 'done')
    
    def testUpdateTaskStatus(self):
        """When moved around, the task status should be updated"""
        # get a task first - todo first
        self.add(title="Hello", des="Hey", status="todo")
        taskToMove = db.session.query(Kanban).filter(Kanban.title=='Hello').first()
        taskId = taskToMove.id

        # todo --> doing
        self.update(id=taskId, new_status="doing")
        holder1 = db.session.query(Kanban).filter(Kanban.id == taskId).first()
        self.assertEqual(holder1.title, "Hello")
        self.assertEqual(holder1.description, "Hey")
        self.assertEqual(holder1.status, "doing")

        # doing --> done
        self.update(id=taskId, new_status="done")
        holder2 = db.session.query(Kanban).filter(Kanban.id == taskId).first()
        self.assertEqual(holder2.title, "Hello")
        self.assertEqual(holder2.description, "Hey")
        self.assertEqual(holder2.status, "done")
    
    def testDeleteTasks(self):
        """Task cannot be found after being deleted"""
        # get a task first
        self.add(title="Hello", des="Hey", status="todo")
        taskToDelete = db.session.query(Kanban).filter(Kanban.title=='Hello').first()
        taskId = taskToDelete.id

        # done!
        self.update(id=taskId, new_status="done")

        # delete
        self.delete(id=taskId)
        holderId = Kanban.query.filter_by(id=taskId).first()
        holderTitle = db.session.query(Kanban).filter(Kanban.title=='Hello').first()
        self.assertIsNone(holderId)
        self.assertIsNone(holderTitle)

if __name__ == '__main__':
    unittest.main()