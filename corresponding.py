
NumberString=input("Enter your string: ")
if NumberString.isalpha():
    print ("your input is string: ", NumberString)
elif NumberString.isdigit():
    Number = int(NumberString)
    print("Your Number is integer: ", Number)
else:
    Number = float(NumberString)
    print ("your Number is float: ", Number)