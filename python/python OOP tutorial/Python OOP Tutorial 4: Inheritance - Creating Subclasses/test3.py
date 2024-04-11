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
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay *self.raise_amount)

class Developer(Employee):
    raise_amount=1.10

    def __init__(self,first,last,pay, programmin_lang):
        super().__init__(first,last,pay)
        self.programmin_lang=programmin_lang

class Manager(Employee):

     def __init__(self,first,last,pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    #you never want to pass mutable datatypes list or dictionary as default arguments(another topic--search about it)

     def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

     def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

     def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname())

    


dev_1 = Developer('Corey','Schaferrr',50000,'Python')
dev_2 = Developer('Test','User',60000,'Java')


mgr_1 = Manager('Sue','Smith',90000,employees=[dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()


#15