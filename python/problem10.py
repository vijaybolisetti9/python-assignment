print("Become the programmer you're meant to be!")


# checking whther pin is valid or not based on cicumstances there should be no digits no spaces and length=4
def valid_pin(pin):
    isvalid=False
    for i in pin:
        if(i=="1"or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9") :
            isvalid=True
            
        if i.isalpha() or i==" " :
            print(i)
            isvalid=False
            break
        
    if isvalid and len(pin)==4:
        return True
    else:
        return False



pin=input()
pin_status=valid_pin(pin)
print(pin_status)