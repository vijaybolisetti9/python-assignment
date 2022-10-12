print("Become the programmer you're meant to be!")

#rotat the value clickwise by 1
no_of_lists=int(input())
for i in range(no_of_lists):
    num_list=input().split(",")  #ex-input=2 5,5,3,6,5
    last_value_index=len(num_list)-1

    last_value=num_list[last_value_index]
    
    new_num_list=[last_value]+num_list[:last_value_index]
    print(new_num_list)