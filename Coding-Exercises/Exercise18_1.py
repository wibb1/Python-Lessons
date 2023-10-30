import PySimpleGUI as sg

label_feet = sg.Text("Enter feet: ")
input_feet = sg.Input()
label_inches = sg.Text("Enter inches: ")
input_inches = sg.Input()
convert_button = sg.Button("Convert")
output_label = sg.Text(key='output_label')
exit_button = sg.Button('Exit', size=5)

layout = [
    [label_feet, input_feet],
    [label_inches, input_inches],
    [convert_button, output_label],
    [exit_button]
]
window = sg.Window('Converter', layout=layout)
while True:
    event, values = window.read()
    if event == 'Exit':
        exit()
    feet = float(values[0]) + float(values[1])/12
    window['output_label'].update(feet * 0.3048)
