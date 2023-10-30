import PySimpleGUI as sg
from zip_tools import extract_archive


sg.theme("Black")

label1 = sg.Text("Select archive")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key='archive')

label2 = sg.Text("Select destination")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key='folder')

extract_button = sg.Button("Extract")
output_label = sg.Text(key='output_label', text_color="green")

window = sg.Window("Archive Extractor Tool",
                   layout=[
                       [label1, input1, choose_button1],
                       [label2, input2, choose_button2],
                       [extract_button, output_label]
                   ])
while True:
    event, values = window.read()
    filepaths = values['archive']
    folder = values['folder']
    extract_archive(filepaths, folder)
    window['output_label'].update("zip file extracted!")

window.close()