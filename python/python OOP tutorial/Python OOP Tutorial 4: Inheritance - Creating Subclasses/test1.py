#we will be learning about inheritance and how to create subclasses. Inheritance allows us to inherit attributes and methods from a parent class. This is useful because we can create subclasses and get all of the functionality of our parents class, and have the ability to overwrite or add completely new functionality without affecting the parents class in any ways. Let's get started.


class Employee:

    num_of_emps = 0
    raise_amount =1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email =first+'.'+last+'@company.com'

    def fullname(self):
        return print('{} {}'.format(self.first, self.last))
    
    def apply_raise(self):
        self.pay = int(self.pay *self.raise_amount)

#when we create a Developer on=bject it going to search for a init method inside Developer class then walk up of chain of inharitance
#this chain called method resolution order
class Developer(Employee):
    raise_amount=1.10
    #not copying code above
    #we are going to let Employee class handle first,last,pay - super().__init__
    #let the Developer set the programming lang
    def __init__(self,first,last,pay, programmin_lang):
        super().__init__(first,last,pay)
        # Employee.__init__(self,first,last,pay) will works same but above more maintainable
        self.programmin_lang=programmin_lang
    


dev_1 = Developer('Corey','Schafer',50000,'Python')
dev_2 = Developer('Test','User',60000,'Java')

print(dev_1.email) 
print(dev_2.email)

#check method resolution order
#print(help(Developer))

#changin raise amount in our sub class it did't had any affect of any Employee instances
print(dev_1.pay) 
dev_1.apply_raise()
print(dev_1.pay)

#init
print(dev_1.programmin_lang) 
print(dev_2.programmin_lang)