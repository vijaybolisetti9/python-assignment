print("Become the programmer you're meant to be!")
#some basic python operators


def operate(num1,num2,operator):
#addition
    if operator=="+": 
        print(num1+num2)
#substraction
    if operator=="-":
        print(num1-num2)
#multiplication
    if operator=="*":
         print(num1*num2)
#division
    if operator=="/":
        print(num1/num2)







num1,num2,operator=input().split()
num1,num2=int(num1),int(num2)
operate(num1,num2,operator)