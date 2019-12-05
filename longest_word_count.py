#wap to that takes list of words and returns the longest word
''''a=input("Enter your sentence:")

c=0
for i in a:
    if i==" ":
        c=c+1

print("the total words in your sentence is: ",c-1)''''' \

#wap to print the longest word in a sentence, with its length
a=input("enter any sentence:")
print(len(max(a.split(), key = len)))

