# Bug-Fixing Exercise 1
# Alina has created a speed calculation function. She traveled a total of 200 miles today which took her two hours. She wants to use her function to calculate the average speed.
#
#
# def speed(distance, time):
#     return distance / time
#
#
# print(speed([200, 4]))
#
# However, when she calls the function (as you see below), she gets an error:
#
# TypeError: speed() missing 1 required positional argument: 'time'
#
# Try fixing the code so she gets 50 as output.

def speed(distance, time):
    return distance / time


print(speed(200, 4))

# Bug - Fixing Exercise 2
# This time, Alina traveled 300 miles and it took her 5 hours. However, she is not getting the correct output from its function. Try fixing the code:
#
#
# def speed(distance, time):
#     return distance / time
#
#
# print(speed(5, 300))


def speed(distance, time):
    return distance / time


print(speed(300, 5))
