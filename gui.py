from PySimpleGUI import Window

import functions
import PySimpleGUI as sg
import time
import os


if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

sg.theme("Black")
clock = sg.Text("", key='clock')
label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
list_box = sg.Listbox(values=functions.read_todos(), key='todos',
                      enable_events=True, size=(45, 10))
add_button  = sg.Button(size=5, image_source='add.png', mouseover_colors="LightBlue2", tooltip="Add todo", key='Add')

edit_button = sg.Button(size=5, image_source='edit.png', mouseover_colors="LightBlue2", tooltip="Edit todo", key='Edit')

done_button = sg.Button(size=5, image_source='complete.png', mouseover_colors="LightBlue2", tooltip="Remove todo", key='Done')

exit_button = sg.Button(size=5, image_source='exit.png', mouseover_colors="LightBlue2", tooltip="Exit Program", key='Exit')

window = sg.Window("My todo app",
                   layout=[[clock], [label], [input_box, add_button], [list_box, edit_button, done_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=100)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case 'Add':
            todos = functions.read_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update("")
        case 'Edit':
            try:
                print(values['todos'])
                todo_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.read_todos()
                index = todos.index(todo_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update("")
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 20))
        case 'Done':
            try:
                todos = functions.read_todos()
                todo_edit = values['todos'][0]
                index = todos.remove(todo_edit)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update("")
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 20))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Exit' | sg.WINDOW_CLOSED:
            break

window.close()
