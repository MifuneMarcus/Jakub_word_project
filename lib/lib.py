import random

def word_parser(word_list):
    """This function processes a list"""

    random_word = random.choice(word_list)

    chose_letter = list(random_word)

    guess_dump = []

    while True:
        guess = input('Please enter a word: ')
        guess_list = list(guess)

        for char in guess_list:
            if char == random_word:
                print(f'You lucky Bastard! The word is {char}')
                exit()
            elif char in chose_letter:
                guess_dump.append(char)
                if guess_dump == chose_letter:
                    print(f'Congrats! You guessed the word, it was {random_word}! You Bastard!')
                    exit()
                print(f'Until now you guessed this letter/s {guess_dump}! You Lucky Bastard!')
                break
            else:
                print(f'Too bad, {guess} has no letters as part of the word. Try again! You Unlucky Bastard!')
                break

