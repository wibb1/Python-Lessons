# Bug Fixing Exercise 1
# The following program (which we developed in today's coding exercise) ends with an error if the user presses the Convert button without supplying any values in the input boxes first.

# import PySimpleGUI as sg
#
#
# def convert(feet, inches):
#     meters = feet * 0.3048 + inches * 0.0254
#     return meters
#
#
# sg.theme("Black")
#
# feet_label = sg.Text("Enter feet: ")
# feet_input = sg.Input(key="feet")
#
# inches_label = sg.Text("Enter inches: ")
# inches_input = sg.Input(key="inches")
#
# button = sg.Button("Convert")
# output_label = sg.Text("", key="output")
# exit_button = sg.Button("Exit")
#
# window = sg.Window("Convertor",
#                    layout=[[feet_label, feet_input],
#                            [inches_label, inches_input],
#                            [button, exit_button, output_label]])
#
# while True:
#     event, values = window.read()
#     match event:
#         case "Exit":
#             break
#         case sg.WIN_CLOSED:
#             break
#     feet = float(values["feet"])
#     inches = float(values["inches"])
#     result = convert(feet, inches)
#     window["output"].update(value=f"{result} m", text_color="white")
#
# window.close()

# Please modify the above program so that instead of ending, the program should show a popup window telling the user
# to enter numbers in the input boxes. In other words, the program should behave as depicted below:


import PySimpleGUI as sg


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


sg.theme("Black")

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input(key="inches")

button = sg.Button("Convert")
output_label = sg.Text("", key="output")
exit_button = sg.Button("Exit")

window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button, exit_button, output_label]])

while True:
    event, values = window.read()
    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
    try:
        feet = float(values["feet"])
        inches = float(values["inches"])
        result = convert(feet, inches)
        window["output"].update(value=f"{result} m", text_color="white")
    except ValueError:
        sg.popup("Please enter only numbers")

window.close()

