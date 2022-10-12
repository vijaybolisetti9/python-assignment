print("Become the programmer you're meant to be!")

def flash(expression):
    arithmetic_index=0
    arithmetic_value=0
    if "+" in expression:
        arithmetic_index=expression.index("+")
        return int(expression[:arithmetic_index]) +int(expression[arithmetic_index+1:])
    elif "-"  in expression:
        arithmetic_index=expression.index("-")
        return int(expression[:arithmetic_index]) - int(expression[arithmetic_index+1:])
    elif "*" in expression:
        arithmetic_index=expression.index("*")
        return int(expression[:arithmetic_index]) * int(expression[arithmetic_index+1:])
    elif "/" in expression:
        arithmetic_index=expression.index("/")
        return int(expression[:arithmetic_index]) // int(expression[arithmetic_index+1:])
            
expression=input()
output=flash(expression)
print(output)