print("Become the programmer you're meant to be!")

def capitalize_word(uncapitalized_word):
    capitalized_word=""
    for i in uncapitalized_word:
        capitalized_word+=(i.upper())
        
    return capitalized_word












uncapitalized_word=input()
capitalized_word=capitalize_word(uncapitalized_word)
print(capitalized_word[::-1])