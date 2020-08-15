# Game 'Guessing number'

import random

guess_num = random.randint(1, 9)

while True:
    usr_command = input('Enter your num: ')

    if usr_command == 'quit':
        break

    if int(usr_command) == guess_num:
        print(f'U win!, guessed num = {guess_num}')
        break
    elif int(usr_command) < guess_num:
        print(f'Your num is: {usr_command}. Too low, try again!')
    elif int(usr_command) > guess_num:
        print(f'Your num is: {usr_command}. Too high, try again!')
