print("Become the programmer you're meant to be!")
class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self,a,b):
        return (a+b)
    def substraction(self,a,b):
        return (a-b)
    def multiplication(self,a,b):
        return (a*b)
    def division(self,a,b):
        return (a/b)
a=int(input())
b=int(input())
calculator_obj=calculator(a,b)
addition=calculator_obj.add(5,5)
substraction=calculator_obj.substraction(5,5)
multiplication=calculator_obj.multiplication(5,5)
division=calculator_obj.division(5,5)

print(addition)
print(substraction)
print(multiplication)
print(division)