print("Become the programmer you're meant to be!")
def flatten_list(listt):
    flattened_list=[]
    for i in listt:
        length=len(i)
        for j in range(length):
            if i[j]=="[" or i[j] =="]" :
                pass
            else:
                flattened_list.append(int(i[j]))
    print(flattened_list)



lists=(["1","[2","3","6","5","4]"],[],["1","[2","3","[6]","5","4]"])



for listt in lists:
    flatten_list(listt)