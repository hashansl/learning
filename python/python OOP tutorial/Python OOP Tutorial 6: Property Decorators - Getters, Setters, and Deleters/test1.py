#Property decorators
#https://www.youtube.com/watch?v=jCzT9XFZ5bw&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=6


class Employee:


    def __init__(self,first,last):
        self.first = first
        self.last = last

    #defining our email in our class like it is a method but we're able to access it like an attribute 
    @property
    def email(self):
        return '{} {}'.format(self.first, self.last)
    @property
    def fullname(self):
        return '{} {}@email.com'.format(self.first, self.last)
    #can't set the attribute without setters
    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete name!!")
        self.first = None
        self.last = None


emp_1 = Employee('John','Smith')


# can't set the attribute without setters
emp_1.fullname ='Corey Schafer'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname