user_prompt1 = "Type add or show: "
user_prompt2 = "Enter a Todo: "
todos = []
while True:
    user_action = input(user_prompt1)
    match user_action.lower():
        case 'add':
            todo = input(user_prompt2)
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break
        case 'stop':
            break
        case 'end':
            break
print("Bye")
