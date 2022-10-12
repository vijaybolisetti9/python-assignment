print("Become the programmer you're meant to be!")
sentence_input= "I have a game.I have a mat.both are going well"
sentence_input= sentence_input.split(".")

word_input=input()
word_input=word_input.lower()
for sentence in sentence_input:
    sentence2=sentence.split(" ")
    for word in sentence2:
        word=word.lower()
        if word==word_input:
            print(sentence)