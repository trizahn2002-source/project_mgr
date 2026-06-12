class Task:

    _id_counter = 1

    def __init__(self, title, assigned_to=""):
        self._id = Task._id_counter
        Task._id_counter += 1
        self._title = title
        self._assigned_to = assigned_to
        self._status = "pending"

    def mark_complete(self):
        self._status = "complete"

    def __str__(self):
        return f"[Task #{self._id}] {self._title} - {self._status}"