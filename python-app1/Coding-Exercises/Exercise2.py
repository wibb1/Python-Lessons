import PySimpleGUI as pg

label1 = pg.Text("Enter feet: ")
label2 = pg.Text("Enter inches: ")
input1 = pg.Input()
input2 = pg.Input()
convert_button = pg.Button("Convert")

window = pg.Window("Convertor", layout=[[label1,input1],[label2,input2],[convert_button]])

window.read()
window.close()
