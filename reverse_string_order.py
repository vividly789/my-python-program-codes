#program to reverse the integer
a=int(input("enter any integer"))
c=0
while a>0:
  b=a%10
  c=b+c*10
  a=a//10
print("the reverse order of ",a, "is",c)
