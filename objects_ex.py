#cards
# class Card:
#     def _init_(self,make,model,noise):
#         self.make = make
#         self.model = model
#         self.noise = noise
#
#     def drive(self):
#         print(self.noise)
#
#     def print_all(self):
#         print self.make, self.model
#         self.drive()
#
# c1 = Card('toyota', 'taco','vroom')
# c2 = Card('ford', 'focus','mas vroom')
#
# c1.print_all()
# c2.print_all()
class Employee:

    def __init__(self, first, last, pay):
        self.first= first
        self.last= last
        self.pay= pay
        self.email =first+ '.'+ last + '@company.com'

    def fullname(self):
        fname=self.first + ' ' +self.last
        return fname  ##use return


emp_1=Employee('Corey','Schafer', 50000)
emp_2=Employee('Colin','OBrien', 51000)

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
