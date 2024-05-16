#Creating Person as base class 

class Person:
    def _init_(self, name, gender, age, cid):
        self._name = name
        self._gender = gender
        self._age = age
        self._cid = cid

#Inheritence principle(subclasses will inherit from person class)

#Encapsulation principle(getter and setter method)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, value):
        self._cid = value

#Abstraction principle(income() in the person class defines functionality that all subclass must implement)

    def income(self):
        raise NotImplementedError("Subclasses should implement this method")

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

class Employee(Person):
    def __init__(self, name, gender, age, cid, salaries):
        super()._init_(name, gender, age, cid)
        self._salaries = salaries

    @property
    def salaries(self):
        return self._salaries

    @salaries.setter
    def salaries(self, value):
        self._salaries = value

    def income(self):
        return self._salaries

class Teacher(Person):
    def __init__(self, name, gender, age, cid, monthly_salary):
        super()._init_(name, gender, age, cid)
        self._monthly_salary = monthly_salary

    @property
    def monthly_salary(self):
        return self._monthly_salary

    @monthly_salary.setter
    def monthly_salary(self, value):
        self._monthly_salary = value

    def income(self):
        return self._monthly_salary * 12  # Annual salary assumed

class Doctor(Person):
    def __init__(self, name, gender, age, cid, yearly_fee):
        super()._init_(name, gender, age, cid)
        self._yearly_fee = yearly_fee

    @property
    def yearly_fee(self):
        return self._yearly_fee

    @yearly_fee.setter
    def yearly_fee(self, value):
        self._yearly_fee = value

    def income(self):
        return self._yearly_fee

class Driver(Person):
    def __init__(self, name, gender, age, cid, daily_rate):
        super()._init_(name, gender, age, cid)
        self._daily_rate = daily_rate

    @property
    def daily_rate(self):
        return self._daily_rate

    @daily_rate.setter
    def daily_rate(self, value):
        self._daily_rate = value

    def income(self):
        return self._daily_rate

# Create instances of different classes
emp = Employee("Mindu", "Male", 35, "10704009876", 50000)
tea = Teacher("Jetshen", "Female", 28, "10706003322", 60000)
doc = Doctor("Dr. Loday", "Male", 45, "10286776556", 1000000)
drv = Driver("karma", "Male", 40, "10705005263", 300)

# Common interface for calculating tax (polymorphic principle)
for person in [emp, tea, doc, drv]:
    print(f"{person.name}'s tax is {person.calculate_tax()}")