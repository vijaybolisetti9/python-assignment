print("Become the programmer you're meant to be!")

 #dicodig a message by multyping the words with specefies number in brackets
message=input()
l=len(message)
start_index=0
end_index=0
new_message=""
multiple_brackets_found=False
end_index2=0
count=0

for i in range(l):
    char=i
    if message[char]=="[":
        start_index=char
        
    if message[char]=="]":
        end_index=char
        count+=1
        if count>1:
            multiple_brackets_found=True
      
        if multiple_brackets_found==False:
            for i in range(start_index):
                new_message+=message[i]
        
        multiplier=int(message[start_index+1])
        decoded_part=multiplier*(message[(start_index+2):end_index])
       
        if multiple_brackets_found==True:
            for i in range(end_index2,start_index):
                new_message+=message[i]
        new_message+=decoded_part
        end_index2=end_index+1
if message[l-1]=="]":
    pass
else:
    for i in range(end_index+1,l):
        new_message+=message[i]

print(new_message)