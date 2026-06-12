from models.person import Person

class User(Person):
    _id_counter = 1
    
    def __init__(self,name,email):
        super().__init__(name,email)
        self._id = User._id_counter
        User._id_counter += 1
        self._projects = []

    def __str__(self):
        return f"[user #{self._id}] {self._name} - {self._email}"