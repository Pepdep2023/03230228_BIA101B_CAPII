class Employee(Person):
    def __init__(self,name,gender,age,cid,salaries):
        super().__init__(name,gender,age,cid)
        self.salaries = salaries

    def income(self):
        return self.salaries