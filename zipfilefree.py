import FreeSimpleGUI as sg
import zipfile
import os

layout = [[sg.Text('Please select the file compresses: ')],
          [sg.Input(key='-Input-Chose-File-'),sg.FilesBrowse('Choose')],
          [sg.Text('Select folder save the files: ')],
          [sg.Input(key='-Input-Folder-Select-'),sg.FolderBrowse('Folder_Browser')],
          [sg.Button('Compress'),sg.Button('Clear'), sg.Button('Quit')]]

window = sg.Window('File System', layout)

while True:
    event, value = window.read()
    if event == sg.WINDOW_CLOSED or event == "Quit":
        break
    elif event == 'Compress':
        files = value['-Input-Chose-File-']
        folder = value['-Input-Folder-Select-']
        if not files or not folder:
            sg.popup_error("⚠️ You must select at least one file and a folder to save the zip.")
            continue
        file_list = files.split(';')
        zip_path = os.path.join(folder, 'compress_file.zip')

        try:
            with zipfile.ZipFile(zip_path, 'w') as zipf:
                for file in file_list:
                    arcname = os.path.basename(file)
                    zipf.write(file, arcname)
            sg.popup('✅ Success', f'Files compressed to:\n{zip_path}')
        except Exception as e:
            sg.popup_error("❌ Compression failed:", str(e))

    elif event == 'Clear':
        window['-Input-Chose-File-'].update('')
        window['-Input-Folder-Select-'].update('') 

window.close()