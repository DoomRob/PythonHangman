# Hangman Game
import random
from collections import Counter

randomWords = '''apple banana mango strawberry orange grape 
pineapple apricot lemon coconut waterlemon cherry papaya 
berry peach lychee muskmelon'''

randomWords = randomWords.split(' ')
# Randomly selects a word from randomWords
word = random.choice(randomWords)

if __name__ == '__main__':
    print('Guess the word! Hint: word is a name of a fruit')

    for i in word:
        # For printing the empty spaces for the letter of the word
        print('_', end =' ')
    print()

    playing = True
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while(chances != 0) and flag == 0:
            print()
            chances -= 1
            try: 
                guess = str(input('Please enter a letter to guess ')) # The flags is uspdated
            except:
                print('Enter only a letter!')
                continue
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter a single letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue
            
            # If the user guessed the letter correctly
            if guess in word:
                l = word.count(guess)
                for _ in range(l):
                    letterGuessed += guess 

            # The word is printed
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1
                elif (Counter(letterGuessed) == Counter(word)):
                    print("The word is: ", end =' ')
                    print(word)
                    flag = 1
                    print("You Win!")
                    break
                    break
                else:
                    print('_', end=' ')
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You lose! Try Again')
            print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print()
        print('Bye! Try Again')
        exit()
