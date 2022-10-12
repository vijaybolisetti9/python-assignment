print("Become the programmer you're meant to be!")
def alternate_sorting(list_1):
    str_list=[]
    num_list=[]
    alternate_list=[]
    for i in list_1:
        if i.isdigit():
            num_list.append(i)
        else:
            str_list.append(i)
    num_list.sort()
    str_list.sort()
    for i in range(len(num_list)):
        alternate_list.append(num_list[i])
        alternate_list.append(str_list[i])
    print(alternate_list)
    
list_1=input().split()
alternate_sorting1=alternate_sorting(list_1)