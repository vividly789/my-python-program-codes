#Wap to input 2numbers and power them(the first number is base and the second number is power)
n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
c=1
for i in range(n2):
    c=n1*c
print("When",n1,"is raised to the power",n2,",the result is","\n",c)
