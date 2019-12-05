letter=input("enter any string: ")
which_letter=input("enter which letter to count: ")
count=0
for i in letter:
    if which_letter==i :
        count=count+1
print("Letter",which_letter, "is repeated", count,"times" )
