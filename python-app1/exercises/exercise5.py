# Please code this exercise in your computer IDE. For this exercise, download the members.txt file attached to the resources. Then, create a program that:
#
# 1. prompts the user to enter a new member.
#
# 2. adds that member to members.txt at the end of the existing members. For example, the user here has entered the member Solomon Right.
#
#
# In the above example, Solomon Right will be added to members.txt updating the content of the file to:
#
# John Smith
# Sen Lakmi
# Sono Octonot
#
# Solomon Right

new_member = input("Enter a new member")+'\n'

file = open('members.txt', 'a')

file.write(new_member)
