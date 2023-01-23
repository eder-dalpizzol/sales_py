import PySimpleGUI as sg
import subprocess


layout = [
    [sg.Text('SysVenda')],
    [sg.Button('Cadastrar Produto', key='add_product', expand_x=True)],
    [sg.Button('Consultar Produtos', key='view_products', expand_x=True)],
    [sg.Button('Inserir Venda', key='add_sale', expand_x=True)],
    [sg.Button('Sair', expand_x=True)]
]

window = sg.Window('SysVenda', layout, size=(None, None), finalize=True)

while True:
    event, values = window.Read()

    if event == 'add_product':
        subprocess.call(['python', 'cadprod.py'])
        
    if event == 'view_products':
        import listprod
        listprod.view_products()


    if event == 'add_sale':
        subprocess.call(['python', 'sales.py'])

    if event == 'Sair' or event is None:
        break

window.Close()
