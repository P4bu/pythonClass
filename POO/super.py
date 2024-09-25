class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def greet(self):
        print("Hello! I am person.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id            

    def greet(self):
        super().greet()
        print(f"Hello! my student ID is {self.student_id}")

student = Student("Pablo", 20, "S231")
student.greet()        