# Please download the three text files a.txt, b.txt, and c.txt from the resources and place them in your computer IDE.
#
# Then, create a program that:
#
# 1. reads each text file and
#
# 2. prints out the content of each file in the command line.
#
# The expected output would be like the following:

filenames = ['a.txt', 'b.txt', 'c.txt']

for index, filename in enumerate(filenames):
    filename = f"exercise7/{filename}"
    file = open(filename, 'r')
    print(file.read())
    file.close()
