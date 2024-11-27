from abc import ABC, abstractmethod

#__ino = private
#class Pojazd2(ABC):
#    def __init__(self,kam)
#    @abstractmethod
#    def info(self):
#        pass
# to jest abstrakt

#class Pojazd(Pojazd2,A,B): <- dziedziczy Samochod, A,B
#   def __init__(self,kam,lol)
#   super().kam
#   self.lol = lol
from Employee import Employee
from EmployeesManager import EmployeesManager
from FrontendManager import *
if __name__ == "__main__":
    app = FrontendManager()
    app.run()

