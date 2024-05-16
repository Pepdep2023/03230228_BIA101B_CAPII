class Teacher(Person):
    def __init__(self,name,gender,age,cid,monthly_salary):
     super().__init__(name,gender,age,cid)
     self.month_salary = monthly_salary

    def income(self):
        return self.monthly_salary * 12 #Annual salary assumpt
    