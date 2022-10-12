print("Become the programmer you're meant to be!")


# deterimine the noof minutes man spends washing his hands while the inputs are no_of_sec he takes to wash his hands daily and no of months he continued his routine
def wash_hands(a,b):
    total_sec=0
    no_of_washes_per_day=int(a)
    no_of_months=int(b)
    for i in range(1,no_of_months+1):
        # as we considered 30 d
        for j in range(1,31):
            total_sec+=(21*5)
    print(total_sec)
    no_of_minutes=total_sec//60
    remaining_sec=total_sec-(no_of_minutes*60)
    return(str(no_of_minutes) +" "+  "minutes" +  " "+ str(remaining_sec)+" "+"seconds")
             


a,b=input().split()
tim_spent=wash_hands(a,b)
print(tim_spent)