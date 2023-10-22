import functions


def main():
    while True:
        todos = functions.read_todos()
        user_prompt1 = functions.set_actions(todos)
        user_action = input(user_prompt1).strip()
        if user_action.startswith('add'):
            todo = user_action[4:] + "\n"
            todos.append(todo)
            functions.write_todos(todos)
        elif user_action.startswith('edit'):
            todo_count = len(todos)
            if todo_count < 1:
                print("Nothing in your todos")
                break
            try:
                index = int(user_action[5:].strip()) - 1
                functions.show_todos()
                if -1 < index < todo_count:
                    prompt = f"Enter the new value for {str(todos[index])}: "
                    new_todo = input(prompt).strip() + "\n"
                    if new_todo == 'quit\n':
                        break
                    todos[index] = new_todo
                    functions.write_todos(todos)
                else:
                    print("Index must be a value between 1 and", todo_count)
                    continue
            except ValueError:
                print("Index must be an integer. Enter like 'edit 1'")
                continue
        elif user_action.startswith('complete') or user_action.startswith('done'):
            todo_count = len(todos)
            if todo_count < 1:
                print("Nothing in your todos")
            else:
                try:
                    if user_action[0] == "c":
                        number = int(user_action[9:])
                    else:
                        number = int(user_action[5:])
                    if number < -1 or number > len(todos):
                        print("Index must be a value between 1 and", todo_count)
                    else:
                        todos.pop(number - 1)
                        functions.write_todos(todos)
                except ValueError:
                    print("Enter an integer")
                    continue
        elif user_action.startswith('show') or user_action.startswith('display'):
            functions.show_todos()
        elif 'exit' in user_action or 'stop' in user_action:
            break
        else:
            print("You have entered an unknown command")
    print("Bye")


if __name__ == '__main__':
    main()
