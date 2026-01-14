"""
Gia Huy Nguyen  
P2
683040746-8
"""
from datetime import datetime
class Person:
    def __init__(self, name, age, birthdate, bloodgroup, is_married):
        self.name = name
        self.age = age
        self._birthdate = birthdate
       
        self.__bloodgroup = bloodgroup
        self.__is_married = is_married
        
        self._id = self.__generate_id()
    def __generate_id(self):
        now = datetime.now()
        self.month = now.month
        self.year = now.year

        new_id = f"{now}{Person._id_running_number:03d}"
        Person._id_running_number += 1
        return new_id
    def display_info(self):
        print(f"ID: {self._id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Birthdate: {self._birthdate}")
class staff(Person):
    def __init__(self, name, age, department, start_year ):
        super().__init__(name, age)
        self.department = department
        self.start_year = start_year
        self.__salary = 0
        self.tenure_year = self.__tenure_year()

    def __tenure_year(self):
        self.tenure_year = datetime.now().year - self.start_year
        return self.tenure_year
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        self.salary = salary 

    def display_info(self):
        