#Static method don't pass anything AUTOMATICALLY
#https://www.youtube.com/watch?v=rq8cL2XMM5M&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=4

class Employee:

    num_of_emps = 0
    raise_amount =1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email =first+'.'+last+'@company.com'

        #since init method run everytime we create a employee
        Employee.num_of_emps +=1

    def fullname(self):
        return print('{} {}'.format(self.first, self.last))
    
    def apply_raise(self):
        self.pay = int(self.pay *self.raise_amount)

    #common convension cls- can't use class
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        #will do the same as Employee(first, last, pay)
        return cls(first, last, pay)

    #don't takes cls,self automatically
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


import datetime
my_date = datetime.date(2016,7,10)

print(Employee.is_workday(my_date))