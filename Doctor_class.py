class Doctor(Person):
    def __init__(self,name,gender,age,cid,yearly__fee):
      super().__init__(name,gender,age,cid)
      self.yearly_fee = yearly_fee

    def income(self):
      return self.yearly_fee
    