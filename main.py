# constant location of the text file
FILE_LOCATION = r'todos.txt'


def main():
    todos = read_todos()
    while True:
        user_prompt1 = set_actions(todos)
        user_action = input(user_prompt1).strip()
        if user_action.startswith('add'):
            todo = user_action[4:] + "\n"
            todos.append(todo)
            write_todos(todos)
        elif user_action.startswith('edit'):
            todo_count = len(todos)
            if todo_count < 1:
                print("Nothing in your todos")
                break
            try:
                index = int(user_action[5:].strip()) - 1
                show_todos(todos)
                if -1 < index < todo_count:
                    prompt = f"Enter the new value for {str(todos[index])}: "
                    new_todo = input(prompt).strip() + "\n"
                    if new_todo == 'quit\n':
                        break
                    todos[index] = new_todo
                    write_todos(todos)
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
                        write_todos(todos)
                except ValueError:
                    print("Enter an integer")
                    continue
        elif user_action.startswith('show') or user_action.startswith('display'):
            show_todos(todos)
        elif 'exit' in user_action or 'stop' in user_action:
            break
        else:
            print("You have entered an unknown command")
    print("Bye")


def set_actions(todos):
    # "Type add, show/display, edit, complete/done or exit/stop: "
    actions = ["Type add [todo's name]"]
    todo_count = len(todos)
    if todo_count:
        actions.append(", show/display, edit [number], complete/done [number]")
    actions.append(" or exit/stop: ")
    return "".join(actions)


def read_todos():
    with open(FILE_LOCATION, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos):
    with open(FILE_LOCATION, 'w') as file:
        file.writelines(todos)


def show_todos(todos):
    item = ""
    if len(todos) > 0:
        for i, item in enumerate(todos):
            text = f"{i + 1}-{item.title()}"
            print(text, end="")
    else:
        print("Nothing in your todos")


if __name__ == '__main__':
    main()
