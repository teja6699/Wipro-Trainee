class EmployeeDetails:
    def __init__(self):
        self.id = 0
        self.ename = 'Teja'
        self.basic_pay = 100000.0
        self.da = 20.0
        self.hra = 10.0
        self.pf = 5.0

    def calculate_allowance(self):
         allowance = (self.basic_pay * self.da / 100) + (self.basic_pay * self.hra / 100)
         return allowance

    def calculate_deduction(self):
         deduction = (self.basic_pay * self.pf / 100)
         return deduction

    def calculate_netsalary(self):
         netsalary = (self.basic_pay * 10)
         return netsalary

