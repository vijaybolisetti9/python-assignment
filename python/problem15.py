print("Become the programmer you're meant to be!")


# converting the camel case to snake case and snake case to camel case

def getcamelcase(input1) :
    camelcase_word=""
    words_list1=input1.split("_")
    
    for word in words_list1:
        
        word=list(word)
        new_word=""
        first_letter=word[0].upper()
        word[0]=first_letter
        for i in word:
            new_word+=i
        camelcase_word+=new_word+" "
        
    print(camelcase_word)
        
       
def getsnakecase(input2):
    snakecase_sentence=""
     
    for i in input2:
        if(i==i.lower()):
            snakecase_sentence+=i
        if(i==i.upper()):
            snakecase_sentence+= ("_"+i.lower())
    print(snakecase_sentence)






input1="he_is_good"
input2="hiAll"
snakecase=getsnakecase(input2)
camelcase=getcamelcase(input1)