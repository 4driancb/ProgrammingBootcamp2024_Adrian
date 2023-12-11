"""
TASK 1

Given a list of digits, determine the integer that it represents.

For example, given the list: [8,3,5,1], your program should output 8351 as an integer.

Note: You are not allowed to use conversion / casting, or any method that makes your solution trivial (such as printing each number without spaces). You should employ an algorithmic approach in your code.
"""

def func(inputList: list):
    # create a variable to output
    output = 0
    # loop through the given list
    for num in inputList:
        # multiply the current number with 10 to add the next number at the back
        output = output * 10 + num
    # output the final number
    return output


print(func([8,3,5,1]))

