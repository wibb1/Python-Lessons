prompt = "Enter your password"
password = input(prompt)
while password != 'password':
    print(False)
    password = input(prompt)
print(True)
