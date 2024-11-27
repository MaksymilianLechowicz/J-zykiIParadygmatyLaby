class Employee:
    def __init__(self,name1,name2,age,salary):
        self.name1 = name1
        self.name2 = name2
        self.age = age
        self.salary = salary

    def infoName2(self):
        return self.name1
    def infoName2(self):
        return self.name2
    def infoAge(self):
        return self.age
    def infoSalary(self):
        return self.salary

    def __str__(self):
        return (f'Pracownik:{self.name1} {self.name2} \t Wiek:{self.age} Wynagrodzenie: {self.salary}')

    def __repr__(self):
        return (f'Pracownik:{self.name1} {self.name2} \t Wiek:{self.age} Wynagrodzenie: {self.salary}')