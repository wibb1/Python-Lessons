# Bug-Fixing Exercise 1
# with open("file.txt", 'r') as file:
#     print(file.read())
#     print(len(file.read()))
# The Python script above is in the same directory with a file named file.txt whose content is:
#
# Hello You
#
# The Python script should print out the content of the file and the number of characters of the text inside file.txt. So, the expected output would be:
#
# Hello You
# 9
# However, the script prints out this:
#
# Hello You
# 0
# Can you fix the program so it prints out the expected output?


with open("file.txt", 'r') as file:
    text = file.read()
print(text)
print(len(text))

