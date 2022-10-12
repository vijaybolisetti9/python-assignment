print("Become the programmer you're meant to be!")

# validating whether number is valid or not

num_input=input().split()

initial_bracket_present=False
final_bracket_present=False
is_valid=False
for i in num_input:
    word=i
    if "(" in word:
        initial_bracket_present=True
        if initial_bracket_present==True and ("(" in word):
            is_valid=True
        if initial_bracket_present==True and (")" not in word):
            is_valid=False
            
print(is_valid)