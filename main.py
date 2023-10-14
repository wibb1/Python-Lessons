user_prompt1 = "Type add, show, or exit: "
user_prompt2 = "Enter a Todo: "
todos = []
while True:
    user_action = input(user_prompt1).strip()
    match user_action.lower():
        case 'add':
            todo = input(user_prompt2)
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break
        case _:
            print("You have entered an unknown command")
print("Bye")
