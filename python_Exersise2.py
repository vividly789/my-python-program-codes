'''Python Assignment 2
1.	Create an empty list and do the following:
a.	Add elements [1,2,’a’,”bat”] to the list
b.	Print length of the list
c.	Add value 45 at index number 2 
d.	Print items with index number 1 to index number 3
e.	What is the difference between pop() and remove()

2.	Given a list [23, 45, 67, 19, 38]. Write a program for following using the built in functions:
a.	Print max value from list
b.	Print min value from list
c.	Sort the list in ascending order
d.	Sort the list in descending order
3.	Without using the built in functions write python program for the above problem (2)

4.	Write a program for following:
a.	Create empty tuple
b.	Can you add items to a tuple? Explain
c.	Create a tuple (1, 12, 55, 12, 81) and iterate through the tuple and print the values to stdout
d.	Check for membership of items ‘55’ and ‘46’ in tuple created in ‘c’

5.	Write a program to compare two lists A and B and print items that are in A but not in B


#ans1
a=[1,2,"a","bat"]
a.insert(2,"45")
print(a[1:4])
print(a)

print(len(a))
for i in range(2,11,2):
    print(i)
    #or
for j in range(0,11):
    if j%2==0:
        print(j)
        
        
        
        
        
        #ans2
a=[23, 45, 67, 19, 38]
print(max(a))
print(min(a))
a.sort()
print(a)
#OR print(a[::-1])
#a.sort(reverse=True)
a.reverse()
print(a)




        #ans3
a=[23, 45, 67, 19, 38]
greater=1
for i in a:
    if greater<i:33
while data_list:
    minimum = data_list[0]  # arbitrary number in list
    for x in data_list:
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)
print(new_list)





#ans4
empty=()
new=(1, 12, 55, 12, 81)
print(55 in new)
print(46 in new)
for i in new:
    print(i)


       #ans5

    a = [1, 2, 'a', 'b', 'c', 3]
    b = [3, 4, 5, 'b', 'e', 'f']
    c = []
    for i in a:
        if i not in b:
            c.append(i)

    print(c)
    '''''#method2
a={1,2,'a','b','c',3}
b={3,4,5,'b','e','f'}
print(b-a)


