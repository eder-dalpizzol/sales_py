import PySimpleGUI as sg
import sqlite3
import os

# Define the layout
layout = [
    [sg.Text('SQLite3 Command'), sg.InputText(key='command')],
    [sg.Button('Execute'), sg.Button('Cancel')]
]

# Create the window
window = sg.Window('SQLite3 Command').Layout(layout)

# Connect to the database
db_dir = os.path.join(os.getcwd(), 'db')
db_path = os.path.join(db_dir, 'db.db')
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Event loop to process user input
while True:
    event, values = window.Read()
    if event == 'Execute':
        try:
            c.execute(values['command'])
            conn.commit()
            sg.Popup("Command executed successfully")
        except sqlite3.Error as e:
            sg.Popup(f'Error: {e}')
    if event == 'Cancel' or event is None:
        break

# Close the cursor and the connection
c.close()
conn.close()

# Close the window
window.Close()
