# A program that checks a certain range of given inputs by the user
# Date: 8.8.20
# Created by Astral

def range_checker():
    user_input = int(input('Please enter a number: '))

    if user_input in range(1,10):
        print('The number enteres is in the collection of numbers')

    else:
        print('Sorry the number you entered is not in the collection of numbers')

range_checker()
