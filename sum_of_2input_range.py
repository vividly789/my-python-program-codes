#wap that takes two integers as input and returns the sum . For example if 0,9 is passed to the function then it should return 45 (0+1+2+3+4+5+6+7+8+9)
a= int(input("enter the lower range:"))
b=int(input("enter the upper range:"))
sum=0
for i in range(b+1):
    if a!=b+1 :
        sum=sum+a
        a=a+1

print("The sum of all the numbers from", a, "to", b, "is",sum)
