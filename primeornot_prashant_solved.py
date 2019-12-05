num=int(input("enter any number"))
count=0;
for i in range(2,num):
    if num%i==0:
        count=1
        break


if count==1:
    print("The number is not prime")
else:
    print("The number is prime")