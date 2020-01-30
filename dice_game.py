import random

min = 1
max = 6


def dice():
    while True:
        print("Rolling the dices...")
        print("The Values are...")
        print(random.randint(min, max))
        print(random.randint(min, max))
        break

dice()

while True:
    user_input = input("Roll again? [Y/N] ")
    if user_input == 'Y' or user_input == 'y':
        dice()
    elif user_input == 'N' or user_input == 'n':
        print('exiting')
        break
    else:
        print('invalid')



