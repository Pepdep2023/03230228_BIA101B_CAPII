class Driver(Person):
    def __init__(self,name,gender,age,cid,daily_rate):
     super().__init__(name,gender,age,cid)
     self.daily_rate = daily_rate

    def income(self):
        return self.daily_rate
    