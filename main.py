from random import choice
from string import ascii_letters


def game():
    words = {'1': ['table', 'It\'s an furniture.', 'Think about kitchen!'],
             '2': ['computer', 'It\'s a device.', 'You should use it right now.'],
             '3': ['tree', 'It\'s a plant.', 'Come on, what a problem? :)'],
             '4': ['display', 'It\'s a device.', 'Look at your display.'],
             '5': ['gallows', 'It\'s an execution "device".', 'And game.'],
             '6': ['horse', 'It\'s an animal.', 'It was very important animal ages ago.'],
             '7': ['bicycle', 'It\'s an transport.', 'And sports equipment.'],
             '8': ['apple', 'It\'s a food.', 'And fruit'],
             '9': ['python', 'It\'s an animal.', 'And programming language...']}
    lives = 6
    guess_word_index = choice(list(words))
    guess_word = list(words[guess_word_index][0])
    playing_list = ['_' for _ in range(0, len(guess_word))]
    print(words[guess_word_index][1])
    used_letters = []

    while lives > 0:
        print(playing_list)
        while True:
            guess_letter = input(f'Letters that you already used {used_letters}\nGuess the letter: ')
            if guess_letter in list(ascii_letters):
                guess_letter.lower()
                break
            else:
                print('Wrong value, you need to input only one letter from the English alphabet.')
        if guess_letter in guess_word:
            print(f'Yes, it\'s correct! Letter {guess_letter} in that word.\n')
            for index, letter in enumerate(guess_word):
                if guess_letter == letter:
                    playing_list[index] = letter
                    guess_word[index] = '_'
                    if '_' not in playing_list:
                        print(f'\nCongrats, you guessed the word {"".join(playing_list)} :)')
                        if input('Do you wanna play again?\t y/n\n') == 'y':
                            game()
                        else:
                            quit()

        else:
            used_letters.append(guess_letter)
            lives -= 1
            print(f'Didn\'t guess, haha :) \t{lives} tries remaining\n')
        if lives == 2:
            print(f'{words[guess_word_index][1]} {words[guess_word_index][2]} ')
        elif lives <= 0:
            print(f'\n{lives} tries remaining, you lose :(')
            if input('Do you wanna play again?\t y/n\n') == 'y':
                game()
            else:
                quit()


game()
