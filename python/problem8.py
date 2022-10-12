print("Become the programmer you're meant to be!")
#changing the key to value and value to key


dict_a={"a":1,"b":2,"c":3}
dict_b={}
for item in dict_a.items():
    key=item[0]
    value=item[1]
    dict_b[value]=key
print(dict_b)