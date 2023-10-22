# Bug-Fixing Exercise 1
# The programmer is trying to extract and print out 'b' using list indexing, but there is an error. Try to fix it.
#
# elements = ['a', 'b', 'c']
# print(elements(1))

elements = ['a', 'b', 'c']
print(elements[1])


# Bug-Fixing Exercise 2
# The code below aims to replace 'b' with 'x' in the list elements.
#
# However, the output of the code is still ['a', 'b', 'c'].
#
# Try to fix the code so 'b' is replaced with 'x'.
#
# elements = ['a', 'b', 'c']
# new = 'x'
# new = elements[1]
# print(elements)


elements = ['a', 'b', 'c']
new = 'x'
elements[1] = new
print(elements)

