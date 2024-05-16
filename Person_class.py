#Creating Person class as a base class representing a person with common attributes like name, gender, age, and cid.

class Person:
    def __init__(self, name, gender, age, cid):
        self.name = name
        self.gender = gender
        self.age = age
        self.cid = cid

# Getter and setter methods for encapsulation being used 


#Abstraction method to be implemented by subclasses
    def income(self):
        raise NotImplementedError ("Subclasses should implement this method")
    
    
    def calculate_tax(self):
        income = self.income()
        if income <= 300000:
            return 0
        elif income < 400000:
            return income * 0.10
        elif income <= 650000:
            return income * 0.15
        elif income <= 1000000:
            return income * 0.20
        elif income <= 1500000:
            return income * 0.25
        else:
            return income * 0.30
    
#Inheritence method will be implemented by following class
class Employee(Person):
    def __init__(self,name,gender,age,cid,salaries):
        super().__init__(name,gender,age,cid)
        self.salaries = salaries

    def income(self):
        return self.salaries

class Teacher(Person):
    def __init__(self,name,gender,age,cid,monthly_salary):
        super().__init__(name,gender,age,cid)
        self.monthly_salary = monthly_salary

    def income(self):
        return self.monthly_salary * 12 #Annual salary assumpt
    
class Doctor(Person):
    def __init__(self,name,gender,age,cid,yearly_fee):
        super().__init__(name,gender,age,cid)
        self.yearly_fee = yearly_fee

    def income(self):
        return self.yearly_fee
    
class Driver(Person):
    def __init__(self,name,gender,age,cid,daily_rate):
        super().__init__(name,gender,age,cid)
        self.daily_rate = daily_rate

    def income(self):
        return self.daily_rate
    

# Create instances of different classes
emp = Employee("Mindu", "Male", 35, "10704009876", 50000)
tea = Teacher("Jetshen", "Female", 28, "10706003322", 60000)
doc = Doctor("Dr. Loday", "Male", 45, "10286776556", 80000)
drv = Driver("karma", "Male", 40, "10705005263", 200)

# Common interface for calculating tax(polymorphic method)
for person in [emp, tea, doc, drv]:
    print(f"{person.name}'s tax is {person.calculate_tax()}")
