user_prompt1 = "Type add, show/display, edit or exit/stop: "
user_prompt2 = "Enter a Todo: "
todos = ['first', 'second', 'third']
while True:
    user_action = input(user_prompt1).strip()
    match user_action.lower():
        case 'add':
            todo = input(user_prompt2)
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                print(item.title())
        case 'exit' | 'stop':
            break
        case 'edit':
            valid = False
            todo_count = len(todos)
            while not valid:
                if todo_count < 1:
                    print("Nothing in your todos")
                    break
                try:
                    index = input("Enter the number from the list you want to edit or quit: ")
                    if index.strip() == 'quit':
                        break
                    index = int(index) - 1
                    if -1 < index < todo_count:
                        prompt = f"Enter the new value for {todos[index]}: "
                        new_todo = input(prompt)
                        todos[index] = new_todo
                        valid = True
                    else:
                        print("Enter a value between one and", todo_count, "or quit")
                except ValueError:
                    print("Enter an integer")
        case _:
            print("You have entered an unknown command")
print("Bye")
