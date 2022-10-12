print("Become the programmer you're meant to be!")
list_a=input().split()
list_b=[]
positive_num_list=[]
for i in list_a:
    list_b.append(int(i))
for i in list_b:
    if i>0:
        positive_num_list.append(i)
positive_num_list.sort()

count=0

for i in range(len(list_b)):
    if (list_b[i]<0):
        pass
    else:
        list_b[i]=positive_num_list[count]
        count+=1
print(list_b)