"""
TASK 2

Create a game where the user must correctly guess a randomly generated integer between 1 and 100.

The user should be notified whether their guess was “lower” or “higher” than the target number.

Note that you will need to use the random library’s randint function.

Remember:
Use functions to group code
Try to have functions that only do one “thing” (e.g. print a message, validate user input, check what message to display)
Check for invalid inputs, notifying the user and re-prompting for a valid input
"""

import random
def guessing_game():
    # set the random number
    number = random.randint(1, 100)

    # create a while loop to prompt for answers
    while True:
        # using the try except else function we can check for incorrect values automatically
        try:
            # first ask for the user's input
            guess = int(input("Guess the random number! "))
        except ValueError:
            # if the user inputs a non-integer
            print("Please choose an integer from 1 to 100")
        else:
            # check if the user's number is correct
            if guess == number:
                return "Correct!"
            # notify the user if the input is not an integer or not in range
            elif guess not in range(1, 101):
                print("Please choose an integer from 1 to 100")
            # notify the user if their guess is lower than the number
            elif guess < number:
                print("Higher!")
            # notify the user if their guess is higher than the number
            else:
                print("Lower!")


print(guessing_game())

