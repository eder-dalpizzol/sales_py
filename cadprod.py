import PySimpleGUI as sg
import sqlite3
import os

def cad_prod(): 
  # Create the form layout
  layout = [
      [sg.Text('Nome Produto', size=(12)), sg.InputText()],
      [sg.Text('Preco', size=(12)), sg.InputText()],
      [sg.Text('Qtde', size=(12)), sg.InputText()],
      [sg.Text('Codigo de Barra', size=(12)), sg.InputText()],
      [sg.Button('Cadastrar'), sg.Button('Cancelar')]
  ]

  # Create the form window
  window = sg.Window('Cadastro de produto').Layout(layout)

  # Event loop to process form input
  while True:
      event, values = window.Read()
      if event == 'Cadastrar':
          # Create the database directory if it doesn't exist
          db_dir = os.path.join(os.getcwd(), 'db')
          if not os.path.exists(db_dir):
              os.makedirs(db_dir)
          
          # Connect to the SQLite database
          db_path = os.path.join(db_dir, 'db.db')
          conn = sqlite3.connect(db_path)
          c = conn.cursor()

          # Create the products table if it doesn't exist
          c.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL, quantity INTEGER, barcode INTEGER);")

          # Insert the product data into the database
          c.execute("INSERT INTO products (name, price, quantity, barcode) VALUES (?, ?, ?, ?)", (values[0], values[1], values[2], values[3]))
          conn.commit()
          conn.close()
          sg.Popup("Produto Cadastrado")
      if event == 'Cancelar' or event == None:
          break

  # Close the form window
  window.Close()
