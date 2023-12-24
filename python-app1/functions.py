# constant location of the text file
FILEPATH = r'todos.txt'
TEST_FILEPATH = f"test_todos.txt"


def set_actions(todos):
    """ checks the to do list length and sets the available actions available  """
    actions = ["Type add [todo's name]"]
    todo_count = len(todos)
    if todo_count:
        actions.append(", show/display, edit [number], complete/done [number]")
    actions.append(" or exit/stop: ")
    return "".join(actions)


def read_todos(filepath=FILEPATH):
    """Read a text file and return the list of items"""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos, filepath=FILEPATH):
    """Write a list to a text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos)


def show_todos(filepath=FILEPATH):
    """print the list of to do items"""
    todos = read_todos(filepath)
    if len(todos) > 0:
        for i, item in enumerate(todos):
            text = f"{i + 1}-{item.title()}"
            print(text, end="")
    else:
        print("Nothing in your todos")


if __name__ == '__main__':
    print("testing functions.py")
    # Test read_todos
    todos = read_todos(TEST_FILEPATH)
    if len(todos) != 5:
        print(f"Fail 1 - todos length is {len(todos)}")
    elif not todos[1] == "second\n":
        print(f"Fail 2 - {todos[1]} != second")
    elif not todos[4] == "fifth\n":
        print(f"Fail 3 - {todos[4]} != fifth")
    else:
        print("read_todos Test Passed")

    # Test set_actions
    actions = set_actions(todos)
    if not actions.__contains__('Type'):
        print("Fail 4 - actions does not include 'Type")
    elif not actions.__contains__("show/display"):
        print("Fail 5 - actions does not include ")
    elif not actions.__contains__("exit/stop"):
        print("Fail 6 - actions does not include exit/stop")
    else:
        print("set_actions Test Passed")

    # test write_todos
    test_todos = read_todos(TEST_FILEPATH)
    test_todos.append("test_todo\n")
    write_todos(test_todos, TEST_FILEPATH)
    new_todos_2 = read_todos(TEST_FILEPATH)

    if test_todos == new_todos_2:
        print("write_todos Test Passed")
    else:
        print(f"Fail 7 - {test_todos} != {new_todos_2}")

    # reset test_todos.txt
    write_todos(todos, TEST_FILEPATH)
