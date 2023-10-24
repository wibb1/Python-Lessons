from PySimpleGUI import Window

import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")

window = sg.Window("My todo app",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case 'Add':
            todos = functions.read_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break

window.close()

