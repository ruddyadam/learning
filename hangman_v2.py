import random

def generateBlanks():


def getRandomWord():
    words = ["pizza", "cheese", "apples"]
    word = words[random.randint(0,len(words)-1)]
    return word

def playWordGame():
    strikes = 0
    maxStrikes = 3
    playing = True

    word = getRandomWord()
    #print(getRandomWord())
    blankedWord = "_" * len(word)


    while playing:
        strikes += 1

        if(strikes >= maxStrikes):
            playing = False

    if strikes >= maxStrikes:
        print('Loser!')
    else:
        print('winner!')

print('Game Started')
playWordGame()
print('Game Over')