from src.models import Kanban
from src.__init__ import app, db
from tests import generalTesting
import unittest

class appFunctionalityTesting(generalTesting):
    def setUp(self):
        super(appFunctionalityTesting, self).setUp()

    def add(self, title, des, status):
        """ request: generally add a task - any status """
        return self.app.post('/add', data=dict(title=title,
                                               description=des,
                                               state=status),
                                     follow_redirects=True)

    def update(self, id, new_status):
        """ request: generally move a task around - any status """
        return self.app.post('/update_state/' + str(id) + '/' + str(new_status),
                          data=dict(id=id, state=new_status),
                          follow_redirects=True)

    def delete(self, id):
        """ request: generally delete any task """
        return self.app.post('/delete/' + str(id), data=dict(id=id), follow_redirects=True)
    
    def testAddTasks(self):
        """ When added, a task should exist at its right category """
        # todo
        self.add(title="Hello", des="Hey", status="todo")
        holder1 = Kanban.query.filter_by(title='Hello').first()
        self.assertEqual(holder1.description, 'Hey')
        self.assertEqual(holder1.status, 'todo')

        # doing
        self.add(title="Hi", des="Hola", status="doing")
        holder2 = Kanban.query.filter_by(title='Hi').first()
        self.assertEqual(holder2.description, 'Hola')
        self.assertEqual(holder2.status, 'doing')

        # done
        self.add(title="Heeyy", des="Helloo", status="done")
        holder3 = Kanban.query.filter_by(title='Heeyy').first()
        self.assertEqual(holder3.description, 'Helloo')
        self.assertEqual(holder3.status, 'done')

    def updateTaskStatus(self):
        """When moved around, the task status should be updated"""
        # get a task first - todo first
        self.add(title="Hello", des="Hey", status="todo")
        taskToMove = Kanban.query.filter_by(title='Hello').first()
        taskId = taskToMove.id

        # todo --> doing
        self.update(id=taskId, new_status="doing")
        holder1 = Kanban.query.filter_by(id = taskId).first()
        self.assertEqual(holder1.title, "Hello")
        self.assertEqual(holder1.description, "Hey")
        self.assertEqual(holder1.status, "doing")

        # doing --> done
        self.update(id=taskId, new_status="done")
        holder2 = Kanban.query.filter_by(id = taskId).first()
        self.assertEqual(holder2.title, "Hello")
        self.assertEqual(holder2.description, "Hey")
        self.assertEqual(holder2.status, "done")
    
    def test_delete(self):
        """Task cannot be found after being deleted"""
        # get a task first
        self.add(title="Hello", des="Hey", status="todo")
        taskToDelete = Kanban.query.filter_by(title='Hello').first()
        taskId = taskToDelete.id

        # done!
        self.update(id=taskId, new_status="done")

        # delete
        self.delete(id=taskId)
        holderId = Kanban.query.filter_by(id=taskId).first()
        holderTitle = Kanban.query.filter_by(title='Hello').first()
        self.assertIsNone(holderId)
        self.assertIsNone(holderTitle)

if __name__ == '__main__':
    unittest.main()