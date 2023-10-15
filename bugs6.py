# Bug - Fixing Exercise 1:
#
# Take a look at the code below:
#
# file = open("data.txt", 'w')
#
# file.write("100.12")
# file.write("111.23")
#
# file.close()
#
#
# The code creates a text file which contains the following content:
#
# 100.12111.23
#
# However, the correct content should be:
#
# 100.12
#
# 111.23
#
# Please fix the code so it creates the file with the correct content.

file = open("data.txt", 'w')

file.write("100.12" + '\n')
file.write("111.23" + '\n')

file.close()


# Bug-Fixing Exercise 2:
# The code below tries to write the string "100.2" to the text file. However, there is an error. Try to fix the error.
#
# file = open("data.txt", 'r')
# file.write("100.12")
# file.close()

file = open("data.txt", 'w')
file.write("100.12")
file.close()
