# 8 characters or longer
# has at least 1 number
# has one uppercase letter
import re
strong_password = False
while not strong_password:
    password = input('Enter a new password: ').strip()
    if len(password) < 8:
        print("Weak password")
    elif not re.search('[0-9]', password):
        print("Weak password")
    elif not re.search('[A-Z]', password):
        print("Weak password")
    elif not re.search('[a-z]', password):
        print("Weak password")
    else:
        print('Strong password')
        strong_password = True
