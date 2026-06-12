class Person:

    def __init__(self,name,email):
        self._name = name
        self._email = email

    def __str__(self):
        return f"{self._name} - {self._email}"