# Coding Exercise 1
# Your task is to create a program that generates a random whole number. Here is how the program should behave:
#
# Enter lower bound:  12
# Enter upper bound:  14
# 14

# As you can see, the program first asks the user to enter a whole number. Then, once the user enters a number,
# the program asks the user again to enter another number.
#
# Then, the program returns a random number that falls between the two whole numbers. Here is another example:
#
# Note: To create this program, you might need to do some internet research or use the Python module index to find
# out what module and what function of that module you can use to generate random numbers. While it is easy for me to
# provide some clues here on what module you should use, searching for information and becoming familiar with
# programming community sites such as Stackoverflow is part of the programming skillset you should acquire. Thus,
# it is essential to practice such skills as well so you are independent after you finish the course.

import random

start = int(input("Enter lower bound: "))
end = int(input("Enter upper bound: "))

ranNum = random.randint(start, end)

print(ranNum)
