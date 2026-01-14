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
        current_year = datetime.date.today().year
        new_id = f"{current_year}{Person._id_running_number:03d}"
        Person._id_running_number += 1
        return new_id
    def display_info(self):
        print(f"ID: {self._id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Birthdate: {self._birthdate}")
class staff(Person):
    def __init__(self, name, age ):
        