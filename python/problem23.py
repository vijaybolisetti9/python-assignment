print("Become the programmer you're meant to be!")

def only_five_and_three(num):
    is_div=False
    
    if (num-5)%3 == 0 or num%5==0 or num%3==0 :
        is_div=True
    return is_div

num=int(input())
is_div=only_five_and_three(num)
print(is_div)