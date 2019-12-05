#count the number of upper case,lower case AND SPACES in a input string:
string=input("enter any string:")
count=0
for i in string:
    if i==i.upper():
        count=count+1

print("The total uppercase characters in",string, "is", count)