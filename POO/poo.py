class Person:
    #Constructor de la clase
    def __init__(self, name, age): 
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age}")

person1 = Person("Ana", 30)
person2 = Person("Luis", 24)

person1.greet()
person2.greet()

