#METHOD1: To remove all the duplicate items in a list
''''a=[1,2,3,'s',2,'d','s',3]
c=[]
for i in a:
    if i not in c:
        c.append(i)
print("The new list without any duplicate elements is:",c)'''''


#METHOD2: To remove all the duplicate items in a list
a=[1,2,3,'s',2,'d','s',3]
b=set(a)
print(b)









