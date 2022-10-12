print("Become the programmer you're meant to be!")

#converting every letter of word to next letter

def con_to_next_letter_words(word):
    alphabets="abcdefghijklmnopqrstuvwxyz"
    new_word=""
    for i in word:
        index=alphabets.index(i)
        index+=1
        new_word+=alphabets[index]
    return new_word
    
word=input()
next_letter_words=con_to_next_letter_words(word)
print(next_letter_words)