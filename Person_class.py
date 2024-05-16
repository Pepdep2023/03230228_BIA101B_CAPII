#Creating Person class as a base class representing a person with common attributes like name, gender, age, and cid.

class Person:
    def __init__(self, name, gender, age, cid):
        self.name = name
        self.gender = gender
        self.age = age
        self.cid = cid


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
    def __init__(self,name,gender,age,cid,yearly__fee):
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
    








