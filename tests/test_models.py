import sys
sys.path.insert(0, ".")

from models.user import User
from models.project import Project
from models.task import Task

def test_user_creation():
    u = User("Alex", "alex@gmail.com")
    assert u._name == "Alex"
    print("test_user_creation passed!")

def test_task_complete():
    t = Task("Build CLI")
    assert t._status == "pending"
    t.mark_complete()
    assert t._status == "complete"
    print("test_task_complete passed!")

def test_project_add_task():
    p = Project("My Project", "Alex")
    t = Task("Do something")
    p.add_task(t)
    assert len(p._tasks) == 1
    print("test_project_add_task passed!")

test_user_creation()
test_task_complete()
test_project_add_task()
print("All tests passed!")