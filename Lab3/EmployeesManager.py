from Employee import Employee


class EmployeesManager:
    def __init__(self):
        self.Emplist = []
    def AddEmplTolist(self):
        print('Podaj dane pracownika')
        name1 = input('Podaj imie')
        name2 = input('Podaj Nazwisko')
        age = input('Podaj wiek')
        salary = input('Podaj wynagrodzenie')
        self.Emplist.append(Employee(name1,name2,age,salary))
    def ViewList(self):
        if len(self.Emplist) == 0:
            print("\nbrak pracowników w bazie")
            return
        else:
            for emp in self.Emplist:
                print(emp)

    def DelFromList(self,agefrom,agetill):
        for emp in self.Emplist:
            if agefrom <= emp.age <= agetill:
                print(f"\tUsunięto pracownika:{emp.name1}")
                self.Emplist.remove(emp)
    def FindEmp(self, name1,name2):
        for emp in self.Emplist:
            if emp.name1 == name1 and emp.name2 == name2:
                return emp
            return None

    def ChangeSalary(self,name1,name2,salary):
        emp =self.FindEmp(name1,name2)
        if emp is None:
            print("Błąd: Nie znaleziono pracownika w bazie")
        else:
            emp.salary = salary

