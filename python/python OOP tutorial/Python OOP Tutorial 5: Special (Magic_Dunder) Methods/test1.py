#Special Methods
#Operator overloading
# __ __ double underscore methods... dunder methods

class Employee:

    raise_amount =1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email =first+'.'+last+'@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay *self.raise_amount)

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return '{}-{}'.format(self.fullname(),self.email)
    
    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','User',60000)

print(emp_1)

print(repr(emp_1))
print(str(emp_1))

print(len('test'))
print('test'.__len__())


print(len(emp_1))