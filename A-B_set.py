
#8.	Write a program to compare two lists A and B and print items that are in A but not in B
a=[1,2,'a','b','c',3]
b=[3,4,5,'b','e','f']
c = []
for i in a:
    if i not in b:
        c.append(i)

print(c)
'''''#method2
a={1,2,'a','b','c',3}
b={3,4,5,'b','e','f'}
print(b-a)'''''


