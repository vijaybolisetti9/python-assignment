print("Become the programmer you're meant to be!")

# capitalizing the first letter of every word
words_input=input().split()
camel_case_output=""
for word in words_input:
    camel_case_word_str=""
    first_letter=(word[0])
    first_letter=first_letter.upper()
    camel_case_word_str+=first_letter
    l=len(word)
    for i in range(1,l):
        camel_case_word_str+=word[i].lower()
    camel_case_output+=camel_case_word_str+" "
print(camel_case_output)