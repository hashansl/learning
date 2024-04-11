#We can think init as constructor
#When we create methods within a class they receive the instances as the first argument
#by convension we use self(can call whatever you want)
#self represents the instance of the class. By using the "self" keyword we can access the attributes and methods of the class in python.
#"__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class.
#Here, the magic keyword "self"  represents the instance of the class. It binds the attributes with the given arguments.
#Usage of "self" in class to access the methods and attributes


class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email =first+'.'+last+'@company.com'

    def fullname(self):
        return print('{} {}'.format(self.first, self.last))
        

emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','User',60000)

print(emp_1.email)
print(emp_2.email)

#printing full name without a method(too much work each time... lets create a method)
#print('{} {}'.format(emp_1.first, emp_1.last))

#need paranthasis here. because fullname is a  method insted of an attribute
emp_1.fullname()
emp_2.fullname()

#we can run methods using class name as well
#this is what happens inteh background--- passes emp_1 as self
Employee.fullname(emp_1)
