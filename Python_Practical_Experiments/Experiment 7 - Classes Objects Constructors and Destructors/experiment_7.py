class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        print("Constructor called")

    def display(self):
        print("Name:", self.name)
        print("Roll number:", self.roll_no)
        print("Marks:", self.marks)

    def __del__(self):
        print("Destructor called")

student1 = Student("Aarav", 101, 85)
student1.display()
del student1
