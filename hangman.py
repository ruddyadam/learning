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
        print('\n')

        g = 0
        t = 0
        answer =[]

        for i in tempAnswer:
            if i == '_':
                if letter == word[g]:
                    answer.append(letter)
                    guessList.append(letter)
                    g = g + 1
                    t = t + 1
                else:
                    answer.append('_')
                    guessList.append(letter)
                    g = g + 1
            else:
                answer.append(i)
                g = g + 1

        if t == 0:
            strike.append('[X]')
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
            print('that was bad!')
        else:
            print('TERRIBLE!!')
        input("\n\npress any key to exit...")
        done = True