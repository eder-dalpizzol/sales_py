import PySimpleGUI as sg
import sqlite3
import os

def view_products():
    # Connect to the SQLite database
    db_dir = os.path.join(os.getcwd(), 'db')
    db_path = os.path.join(db_dir, 'db.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Retrieve all products from the products table
    c.execute("SELECT * FROM products")
    products = c.fetchall()

    # Create a list of product names
    product_list = [[product[1], product[2], product[3], product[4]] for product in products]

    # Create the layout for the product view window
    layout = [
        [sg.Table(values=product_list, headings=['Name', 'Price', 'Quantity', 'Barcode'], auto_size_columns=True, key='product_table')],
        [sg.Button('OK')]
    ]

    # Create the product view window
    window = sg.Window('View Products').Layout(layout)

    # Event loop to process user input
    while True:
        event, values = window.Read()
        if event == 'OK' or event == None:
            break

    # Close the product view window
    window.Close()

