#when we access class variables we need to acccess them through either class itself or instance of the class
#Employee.raise_amount or self.raise_amount


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
        #can use self.raise_amount and Employee.raise_amount both (first check the instance then goes to class)
        self.pay = int(self.pay *Employee.raise_amount)
        

emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','User',60000)

#print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)

#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)

#I can access my class varibles both my class itself as well as both instances
#Wehen we access and attribute it will first check if the instance contains that attribute and if it dosent it will see if the class or any class that it inherit from contains that attribute

#namespace (these are the values they return)
print(emp_1.__dict__)

#namespace (these are the values they return)
#print(Employee.__dict__)

Employee.raise_amount=2

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print('--------')

#only change raise amount for employee 1
emp_1.raise_amount=3
print(emp_1.__dict__)


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


print('--------')
print(Employee.num_of_emps)