#regular methods in a class automatically take the instance as the first argument and by convension we are calling this self
#How can we change that it instend automatically takes the class as the first argument??
#WE GOING TO USE CLASS METHOD TO THAT, TURN REGULAR METHOD TO CLASS METHOD



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

        

emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','User',60000)

#Now we are working with the class instead of the instance
#This is equal to Employee.raise_amount = 1.05 (insted we use  below code )
Employee.set_raise_amt(1.05)
#we can run class method from instance but no point


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

