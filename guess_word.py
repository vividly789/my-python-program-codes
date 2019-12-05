#guess a secret word FOR 3 ATTEMPS
guess =("master")
choise=""
count=0
while choise.upper() !=guess.upper() :
    choise=input("Guess the secret word:")
    count+=1
    while count>3:
        print("sorry all your attemps finished")
        exit()
print("you win")

s

