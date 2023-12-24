# Bug - Fixing Exercise 1
# Supposedly, the following program should:
#
# 1. Prompt the user to input an index(e.g., 0, 1, or 2).
# 2. Print out the item with that index.
#
# However, there is a bug with the program which you should try to fix.
#
# menu = ["pasta", "pizza", "salad"]
#
# user_choice = input("Enter the index of the item: ")
#
# message = f"You chose {menu[user_choice]}."
# print(message)

menu = ["pasta", "pizza", "salad"]

user_choice = int(input("Enter the index of the item: "))

message = f"You chose {menu[user_choice]}."
print(message)

# Bug - Fixing Exercise 2
# Here is another piece of buggy code:
#
# menu = ["pasta", "pizza", "salad"]
#
# for i, j in enumerate[menu]:
#     print(f"{i}.{j}")#

menu = ["pasta", "pizza", "salad"]

for i, j in enumerate(menu):
    print(f"{i}.{j}")

# Fix the code, so it prints out the output below:
# 0.pasta
# 1.pizza
# 2.salad
#
#
# Bug - Fixing Exercise 3
# Here is another piece of code that contains a bug:
#
# menu = ["pasta", "pizza", "salad"]
#
# for i, j in enumerate(menu):
#     print("f{i}.{j}")

menu = ["pasta", "pizza", "salad"]
for i, j in enumerate(menu):
    print(f"{i}.{j}")

# The expected output is this:
#
# 0.pasta
# 1.pizza
# 2.salad
# Fix the bug so the program prints out the above output.

