#In here problem is we get string as information and we don't want parse string everytime we create employee
#let's create alternative constructor that allows them to create a object for them
# USE CLASS METHODS AS ALTERNATIVE CONSTRUCTOR HERE

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


        

emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','User',60000)


emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-3000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)

new_emp_2 = Employee.from_string(emp_str_2)


print(new_emp_1.email)
print(new_emp_2.email)

