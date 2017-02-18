import random


minNumber = 12
maxNumber = 43
magicNumber = random.randint(minNumber,maxNumber)
message = "The magic number is between {0} and {1}"
print(message.format(minNumber, maxNumber))
print("Hello, what is your favorite number?")
number = input()

#print("Your favorite number is " + number)

print("the magic number is " + str(magicNumber))

found = False

while not found:
    print("Guess what it is!")
    guess = int(input())
    if guess == magicNumber:
        found = True
        print("You guessed it!")
    elif guess < magicNumber:
        print("too low!  guess again")
    else:
        print("too high!  guess agin!")



