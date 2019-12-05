# method1to eliminate duplicate elements in a list
'''listOfNums=[1,"no",98,"ji",7,8,"no",1,98,8,0,"90",76,1,80,98]
#Convert list to set and then back to list
listOfNums = list(set(listOfNums))
print(listOfNums)'''

test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print("The original list is : " + str(test_list))

# using naive method
# to remove duplicated
# from list
res = []
for i in test_list:
    if i not in res:
        res.append(i)

print("The list after removing duplicates : " + str(res))


