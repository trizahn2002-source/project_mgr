from models.task import Task

class Project:

    _id_counter = 1

    def __init__(self, title, owner_name, description="", due_date=""):
        self._id = Project._id_counter
        Project._id_counter += 1
        self._title = title
        self._owner_name = owner_name
        self._description = description
        self._due_date = due_date
        self._tasks = []

    def add_task(self, task):
        self._tasks.append(task)

    def to_dict(self):
        return {
            "id":  self._id,
            "title": self._title,
            "owner_name": self._owner_name,
            "description":nself._description,
            "due_date": self._due_date,
            "tasks": [t.to_dict() for t in self._tasks]
        }

    def __str__(self):
        return f"[Project #{self._id}] {self._title} - owner: {self._owner_name}"