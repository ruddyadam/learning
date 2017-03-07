import sys

pyVersion = sys.version_info[0]
pySubVersion = sys.version_info[1]
message = '\n********\nYou are currently running Python version {0}.{1}\n********\n'

print(message.format(pyVersion,pySubVersion))

if sys.version_info < (3, 0):
    raise ValueError("you must use python 3.x")

else:
    print("good\n")

guessList = []
tempAnswer = ''
answer = []
strikeList = []
strike = []
letter = ''
done = False

print('Starting game!')

#to allow the user to enter a secret word, uncomment here
word = input('Enter a secret word: ')
print('\n' * 100)

#to hardcode a single word, uncomment here
#word = 'steinsgate'

for i in word:
    tempAnswer = tempAnswer + '_'
    answer.append('_')
print('%s' % ' '.join(map(str,tempAnswer)))
#print(answer)

while done == False:

    if '_' in answer:

        print('%s' % ' '.join(map(str, strike)))
        letter = input('Guess a letter!\n')
        if not letter in guessList:
            guessList.append(letter)

        #print('guessed letters: ' + )
        print('\n')

        g = 0 #used to iterate through ther letters of the secret word
        t = 0 #used to find if the letter input was in the secret word
        answer =[]

        for i in tempAnswer:
            if i == '_':
                if letter == word[g]:
                    answer.append(letter)
                    t = t + 1 #this iterates if a new letter was found in the puzzle
                else:
                    answer.append('_')
            else:
                answer.append(i)
            g = g + 1

        if t == 0:
            strike.append('['+letter+']') #caleb suggested this change to keep track of letters!!  2-27-17
        tempAnswer = answer

        print('%s' % ' '.join(map(str, answer)))
#    elif :

    else:
        print('You got it!')
        print('The secret word is: ' + word)
        print('and it only took you ' + str(len(strike)) + ' strikes!')
        if len(strike) < 3:
            print('Wow!! Great job!')
        elif len(strike) < 11:
            print("ok, that's ok.")
        elif len(strike) < 21:
            print('That was bad!')
        else:
            print('YOU ARE TERRIBLE!!')
        input("\n\npress any key to exit...")
        done = True