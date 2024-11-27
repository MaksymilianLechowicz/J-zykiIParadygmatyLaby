from EmployeesManager import *
from utility import *
class FrontendManager:
    def __init__(self):
        self.EmployeesManager = EmployeesManager()

    def Program(self):
        print("\nZarządzanie pracownikami\n")
        message =[
            '1. Dodaj pracownika',
            '2. Wyświetl pracowników',
            '3. Usuń pracownika',
            '4. Aktualizuj wynagrodzenie pracownika',
            '5. Wyjście'
        ]
        print('\n'.join(message))
        msg = f"Wybierz opcje (1 -{len(message)}): "
        return inputValue(msg,1,len(message))

    def run(self):
        while True:
            choice = self.Program()
            if choice == 1:
                self.EmployeesManager.AddEmplTolist()
            elif choice == 2:
                self.EmployeesManager.ViewList()
            elif choice == 3:
                age1 = int(input("Podaj początkowy wiek"))
                age2 = int(input("Podaj końkowy wiek"))
                self.EmployeesManager.DelFromList(age1,age2)
            elif choice == 4:
                name1 = input("Podaj Imie pracownika")
                name2 = input("Podaj Nazwisko pracownika")
                sal = int(input("Podaj nowe wynagrodzenie"))
                self.EmployeesManager.ChangeSalary(name1,name2,sal)
            elif choice == 5:
                break
            else:
                print("Wybrałeś zły numer")
                continue