#print the multiplication of a number
m=int(input("enter any number"))
print("the multiplication table of ", m, "is")
mul=1
if m<0 :
    print("the multiplication table dosesnt exists")
elif m==0 :
    print("sorry")
else:
    for i in range(1,11):
        mul=m*i
        print(m,"*",i,"=",mul)