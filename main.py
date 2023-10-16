# constant location of the text file
FILE_LOCATION = r'todos.txt'
def main():
    todos = read_todos()
    while True:
        user_prompt1 = set_actions(todos)
        user_action = input(user_prompt1).strip()
        match user_action.lower():
            case 'add':
                todo = input("Enter a Todo: ")
                todos.append(todo)
            case 'show' | 'display':
                show_print(todos)
            case 'exit' | 'stop':
                break
            case 'edit':
                valid = False
                todo_count = len(todos)
                show_print(todos)
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
                            prompt = f"Enter the new value for {str(todos[index])}: "
                            new_todo = input(prompt) + "\n"
                            todos[index] = new_todo
                            valid = True
                        else:
                            print("Enter a value between 1 and", todo_count, "or quit")
                    except ValueError:
                        print("Enter an integer")
            case 'complete' | 'done':
                show_print(todos)
                if len(todos):
                    try:
                        number = int(input("Number of the completed todo: "))
                        todos.pop(number - 1)
                    except ValueError:
                        print("Enter an integer")
            case _:
                print("You have entered an unknown command")
    write_todos(todos)
    print("Bye")


def set_actions(todos):
    # "Type add, show/display, edit, complete/done or exit/stop: "
    actions = ["Type add"]
    todo_count = len(todos)
    if todo_count:
        actions.append(", show/display, edit, complete/done")
    actions.append(" or exit/stop: ")
    return "".join(actions)


def read_todos():
    with open(FILE_LOCATION, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos):
    with open(FILE_LOCATION, 'w') as file:
        file.writelines(todos)


def show_print(todos):
    if len(todos) > 0:
        for i, item in enumerate(todos):
            text = f"{i + 1}-{item.title()}"
            print(text, end="")
    else:
        print("Nothing in your todos")


if __name__ == '__main__':
    main()
