class Person:
    def __init__(self, name):
        self.name = name

    def show_role(self):
        print(self.name, "is a person")

class Student(Person):
    def show_role(self):
        print(self.name, "is a student")

class Teacher(Person):
    def show_role(self):
        print(self.name, "is a teacher")

people = [Student("Aarav"), Teacher("Meera")]
for person in people:
    person.show_role()
