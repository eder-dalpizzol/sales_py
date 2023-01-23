import PySimpleGUI as sg
import sqlite3
import os

# Connect to the database
db_dir = os.path.join(os.getcwd(), 'db')
db_path = os.path.join(db_dir, 'db.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Query the products table
cursor.execute("SELECT * FROM products")
products = cursor.fetchall()

# Create a list of product names to use in the ComboBox
product_list = [product[1] for product in products]

layout = [
    [sg.Text('Cliente', size=(12)), sg.InputText(key='customer_name')],
    [sg.Text('Produto', size=(12)), sg.Combo(product_list, key='product', expand_x=True)],
    [sg.Text('Quantidade', size=(12)), sg.InputText(key='quantity', size=(5)), sg.Push(), sg.Text('Preco', size=(9)), sg.InputText(key='sale_value', size=(5))],
    [sg.Button('Add', size=(9)), sg.Button('Cancel', size=(9))],
    [sg.Text('Itens da Venda', font=("Helvetica", 15))],
    [sg.Listbox(values=[], key='sale_items', size=(40, 10), expand_x=True)],
    [sg.Text('Total da Venda: ', font=("Helvetica", 15)), sg.Text('', key='total_purchase',font=("Helvetica", 15), size=(15, 1))],
    [sg.Button('Confirmar Venda'), sg.Button('Cancelar Venda')]
]

# Create the window
window = sg.Window('Add Sale').Layout(layout)

# Create a list to store sale items
sale_items = []
sale_number = 1
total_purchase = 0

# Event loop to process user input
while True:
    event, values = window.Read()
    if event == 'Add':
        sale_value = values['sale_value']
        quantity = values['quantity']
        customer_name = values['customer_name']
        product = values['product']
        sale_items.append((sale_value, quantity, customer_name, product))
        total_purchase += float(sale_value)*float(quantity)
        window.FindElement('sale_items').Update(sale_items)
        window.FindElement('total_purchase').Update(total_purchase)
    if event == 'Confirm Sale':
        # Insert sale items into the sales table
        cursor.executemany("INSERT INTO sales (sale_value, quantity, customer_name, product, sale_number) VALUES (?,?,?,?,?)", [(value[0], value[1], value[2], value[3], sale_number) for value in sale_items])
        conn.commit()
        sale_number += 1
        sale_items = []
        total_purchase = 0
        window.FindElement('sale_items').Update(sale_items)
        window.FindElement('total_purchase').Update(total_purchase)
        sg.Popup("Venda Confirmada")
    if event == 'Cancelar Venda':
        sale_items = []
        total_purchase = 0
        window.FindElement('sale_items').Update(sale_items)
        window.FindElement('total_purchase').Update(total_purchase)
    if event == 'Cancelar Venda' or event is None:
        break
    if event == 'product':
        selected_product = values['product']
        cursor.execute("SELECT price FROM products WHERE name=?", (selected_product,))
        result = cursor.fetchone()
        window.FindElement('sale_value').Update(result[0])

# Close the cursor and the connection
cursor.close()
conn.close()

# Close the window
window.Close()
