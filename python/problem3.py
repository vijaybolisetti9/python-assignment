# program to take a number n and return nth even number

print("Become the programmer you're meant to be!")
num=int(input())

nth_num=0
even_num_count=0
while even_num_count<num:
    nth_num+=1
    if nth_num%2==0:
        even_num_count+=1
    
print(nth_num)