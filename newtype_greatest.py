# Method <1>to print greatest number out of 3
def greatest_num():
  n1 = int(input())
  n2= int(input())
  n3 = int(input())

  if n1 > n2 and n1 > n3 :
    return n1
  elif n2 > n1 and n2 > n3:
    return n2
  else:
    return n3
print("the greatest number is",greatest_num())



# Method <2>to print greatest number out of 3
'''print("input the 3 numbers")
n1,n2, n3= int(input()), int(input()),int(input())
def greatest_num(n1,n2,n3):
  if n1 > n2 and n1 > n3 :
    return n1
  elif n2 > n1 and n2 > n3:
    return n2
  else:
    return n3
print("Greatest Number -s :", greatest_num(n1,n2,n3))'''


# Method <3>to print greatest number out of many
'''l1 = []
num = int(input('How many numbers: '))
for i in range(num):
    l2 = int(input('Enter numbers'))
    l1.append(l2)
print("Maximum element in the list is :", max(l1))'''






















