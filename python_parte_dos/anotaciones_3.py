class Employee: 
    name: str
    age: int
    salary: float

    def __init__(self, name:str, age:int, salary:float):
        self.name = name
        self.age = age
        self.salary = salary

    def introduce(self) -> str:
        return f'Hola, me llamo {self.name} tengo {self.age} años'
    
employee1 = Employee('Carlos', 30, '35000.00')
print(employee1.introduce())