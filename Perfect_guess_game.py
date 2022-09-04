# Perfect Guess game
# Author is Rahul
# date 07-03-2022

name=input("Enter your name to play this game\n")
import random
randNumber=random.randint(1,100)
userGuess=None
guesses=0

print(randNumber)

while(userGuess!=randNumber):
    try:
        userGuess=int(input("Enter your guess:  "))
        guesses+=1
        if (userGuess==randNumber):
            print("You guessed it right!")
        else:
            if (userGuess>randNumber):
                print("You guessed it wrong. Enter smaller number")
            else:
                print("You guessed it wrong. Enter a larger number")
    except ValueError:
        print("Please enter a valid number")

# Print how many guesses you took to guess it right
print(f"{name} guessed it right in {guesses} guesses")

with open("hiscore.txt") as f:
    hiscore=f.read()

if (guesses<int(hiscore)):
    print(f"{name} just broke the hiscore!")
    with open("hiscore.txt","w") as f:
        f.write(str(guesses)) #Remember to add string
        f.close()