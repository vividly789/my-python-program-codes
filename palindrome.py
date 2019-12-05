#to check whether the given word is palindrome or not
w=input("enter any word")
l=len(w)
print(w)
c=w
d=w[::-1]
c="".join(c.split())
d="".join(d.split())
if c==d :
    print("the input word is palindrome")
else:
    print("not palindrome")
