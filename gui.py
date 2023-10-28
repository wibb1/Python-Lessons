from PySimpleGUI import Window

import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.read_todos(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button('Edit')
done_button = sg.Button('Done')
exit_button = sg.Button('Exit')
window = sg.Window("My todo app",
                   layout=[[label], [input_box, add_button], [list_box,edit_button,done_button], [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case 'Add':
            todos = functions.read_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update("")
        case 'Edit':
            todo_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.read_todos()
            index = todos.index(todo_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update("")
        case 'Done':
            todos = functions.read_todos()
            todo_edit = values['todos'][0]
            index = todos.remove(todo_edit)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update("")
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Exit' | sg.WINDOW_CLOSED:
            break

window.close()

