print("Become the programmer you're meant to be!")

#reversing a string without affecting the special characters


def special_str(word):
    list_of_normal_characters=[]
    list_of_special_characters=[]
    count=0
    for i in word:
        if (i=="@" or i=="$" or i=="%" or i=="&"):
            list_of_special_characters.append(i)
        else:
            list_of_normal_characters.append(i)
    list_of_normal_characters=list_of_normal_characters[::-1]
    print()
    for i in range(len(word)):
        if word[i] in list_of_special_characters:
            pass
        else:
            word[i]=list_of_normal_characters[count]
        count+=1
        if count==len(list_of_normal_characters):
            break
    return (word)

word=list(input())
special_str=special_str(word)
print(special_str)