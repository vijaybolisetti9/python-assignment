print("Become the programmer you're meant to be!")


#creating the program to take two inputs if both of them are strings add them if both of them are integers concatenate them
def stupid_addition(a,b):
    if(a==int(a) and  b==int(b)):
        return(str(a)+str(b))
    if(a!=int(a) and  b!=int(b)):
        a=int(a)
        b=int(b)
        return(a+b)
    
    
a=int(input())
b=int(input())
str_a=str(a)
str_b=str(b)
stupid_addition1=stupid_addition(a,b)
stupid_addition2=stupid_addition(str_a,str_b)
print(stupid_addition1)
print(stupid_addition2)