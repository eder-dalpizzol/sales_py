import PySimpleGUI as sg
import cadprod, listprod, sales, create_db

create_db.db()

sg.theme('LightBlue')

layout = [
    [sg.Text('SysVenda')],
    [sg.Button('Cadastrar Produto', key='add_product', expand_x=True)],
    [sg.Button('Consultar Produtos', key='view_products', expand_x=True)],
    [sg.Button('Inserir Venda', key='add_sale', expand_x=True)],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Button('Sair', expand_x=True)]
]

window = sg.Window('SysVenda', layout, size=(600, 245), finalize=True)

while True:
    event, values = window.Read()

    if event == 'add_product':
        cadprod.cad_prod()
        
    if event == 'view_products':
        listprod.view_products()

    if event == 'add_sale':
        sales.sales()

    if event == 'Sair' or event is None:
        break

window.Close()
