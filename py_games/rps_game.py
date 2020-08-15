# Game "rock, paper, scissors"
import random


variables = ['rock', 'paper', 'scissors']


while True:
    usr_command = input('Enter your command: ')
    computer = random.choice(variables)
    if usr_command == 'quit':
        break
    else:
        print(f'You typed: {usr_command}')

    if usr_command == 'rock' or usr_command == 'paper' or usr_command == 'scissors':
        print(f'Computer typed: {computer}')
    else:
        print('Unknown command, try again!')
        break

    if usr_command == computer:
        print('Draw!')
    elif usr_command == 'rock' and computer == 'paper':
        print('Computer win!')
    elif usr_command == 'paper' and computer == 'scissors':
        print('Computer win!')
    elif usr_command == 'scissors' and computer == 'rock':
        print('Computer win!')
    else:
        print('User win!')
