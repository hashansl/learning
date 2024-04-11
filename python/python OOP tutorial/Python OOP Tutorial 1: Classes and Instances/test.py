#if you want to keep a class empty(without an error) for time use "pass"

class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)
#These two instances have two different memory locations

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'coreysch@gmail.com'
emp_1.pay =50000


emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'testuser@gmail.com'
emp_2.pay =60000

print(emp_1.email)
print(emp_2.email)

# We dont get much benifit if we do classes this way