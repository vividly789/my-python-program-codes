#to print the even and odd number from a certain range of numbers
first=int(input("enter the lower range"))
last=int(input("enter the upper range"))
print("The list of even numbers are :")
for even in range(first,last+1):
    if even%2==0:
        print(even , end=" ")

print("The list of odd numbers are : ")
for odd in range(first,last+1) :
    if odd%2!=0 :
        print(odd, end=" ")


