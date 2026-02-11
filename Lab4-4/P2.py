"""
Gia Huy Nguyen
683040746-8
P2
"""
# Error handling:
# isintance(object, classinfo)
# try - except ZeroDivisionError: Dividing by zero
#ValueError: Wrong value type (e.g., int("hello"))
#TypeError: Wrong data type for operation
#FileNotFoundError: File doesn't exist
#KeyError: Dictionary key doesn't exist
#"_" = weakly private = "#", "__"truly private = "-"" in uml
t = 0
n = input("Enter 5 temps in Celcius: ").split()
if len(n) != 5:
    print("Please input exactly 5 numbers")
else:
    for i in n:
        try: 
            i = float(i)
            t += i
        except ValueError as e:
            t = 0
            print(f"Catch ValueError: {e}")
            break
try:
    avg = t/len(n)
except:
    print("Please input exactly 5 numbers")

if t != 0:
    print(f"Average temperature = {avg:.2f} Celsius")


from abc import ABC, abstractmethod


class vehicle(ABC):
    def __init__(self, make, model, year, is_running = False):   #Parameter  # Boolean: True,False
       #instance attribute
        self.make = make
        self.model = model
        self.year = year
        self.is_running = is_running
    #class method
    @abstractmethod
    def start_engine(self):
        """start enginee""" #expand method
        pass
    
    @abstractmethod
    def stop_engine(self):
        """stop the vehicle's engine"""
        pass

    def get_info(self):
        return f"Year: {self.year} \nMake: {self.make} \nModel: {self.model}"
    
class CommercialVehicle:  #super class
    def __init__(self, license_number, max_load): #initializer
        
        self.max_load = max_load
        self.license_number = license_number
        self.current_load = 0 # non-parameter
    def start_engine(self):
        self.is_running = True
        return "started"
    def stop_engine(self):
        self.is_running = False
        return "stopped"
    def load_cargo(self, weight):
        if weight > 0 and (self.current_load + weight <= self.max_load):
            self.current_load += weight
            return True
        return False
    def unload_cargo(self, weight):
        if weight > 0 and (self.current_load - weight >= 0):
            self.current_load -= weight
        self.current_load = 0
        return self.current_load
class Car(vehicle):
    def __init__(self, num_doors, *args, **kwargs):  # *= Tuple, ** = List
        super().__init__(*args, **kwargs)  
        self.num_doors = num_doors
    def start_engine(self):
        self.is_running = True
        return "start engine"
    def stop_engine(self):
        self.is_running = False
        return "stop engine"
    
class Trailer(CommercialVehicle):
    def __init__(self, num_axles = 2, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.num_axles = num_axles
    def get_weight_per_axles(self):
        if self.num_axles <=0:
            return 0
        return self.current_load / self.num_axles
    """Calculates the final price after applying a discount.

    Args:
       none
    Returns:
        float: The price after applying the discount

    Raises:
        ValueError: If discount_rate is not between 0 and 100

    Examples:
        >>> calculate_discount(100, 20)
        80.0
    """
class DeliveryVan(Car, CommercialVehicle, ):
    def __init__(self, make, model, year, license_number, max_load, num_doors, is_running = False):
        super().__init__(license_number=license_number, max_load=max_load, make=make, model=model, year=year, is_running=is_running, num_doors=num_doors)
        self.delivery_mode = False
    def toggle_delivery_mode(self):
        self.delivery_mode = not self.delivery_mode
        return f"Delivery mode is {self.delivery_mode}"
    def begin_service(self):
        print(self.get_info())
        print(f"Loading in a cargo: {self.load_cargo(5000)} kg")
        print(self.start_engine())
        print(self.toggle_delivery_mode())
        print(self.stop_engine())
        print(f"Unloading the cargo{self.unload_cargo(1000)} kg")
        print(self.toggle_delivery_mode())
if __name__ == "__main__":
    Bill = DeliveryVan("Fifa", "Tintrai", 2008,"683040746-8", 10000, "4", is_running = False  )
    Bill.begin_service()




    #OOP 2
class Employee:
    company = "TechCorp"  # Class variable
    total_employees = 0   # Tracks total employees

    def __init__(self, name, salary): #constructor
        # Instance method
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def get_salary(self):  # Instance method
        return self.salary

    @classmethod
    def from_string(cls, emp_string):
        # Class method - alternative constructor
        name, salary = emp_string.split('-')
        return cls(name, int(salary))

    @classmethod
    def get_company_name(cls):
        # Class method - accessing class variable
        return cls.company

    @staticmethod
    def validate_salary(salary):
        # Static method - utility function
        return salary > 0

# Usage
emp1 = Employee("Alice", 50000)  # Regular constructor
emp2 = Employee.from_string("Bob-60000")  # Class method constructor

print(emp1.get_salary())  # Instance method
print(Employee.get_company_name())  # Class method
print(Employee.validate_salary(55000))  # Static method