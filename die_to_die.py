# %%
import secrets
import PySimpleGUI as sg

#%%
def rolar(quantia, dado):
    """números aleatórios uma quantia de vezes"""
    resultado = []
    for i in range(quantia):
        a = secrets.choice(range(1, dado))
        resultado.append(a)
    return resultado

# %%
sg.theme('Reddit')
layout = [
    [sg.Text('Numdados'), sg.Input(size=(20,1), key='-QUANT-')],
    [sg.Text('Dado'), sg.Input(size=(20,1), key='-DIE-')],
    [sg.Text('Resultado:'),sg.Output(size=(30,20), key='-OUTPUT-')],
    [sg.Button('Rolar'),sg.Button('Limpar'), sg.Button('Sair')]
]

window = sg.Window('Die to die', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    if event == 'Rolar':
        a = rolar(int(values['-QUANT-']), int(values['-DIE-']))
        print(a)
    
    if event == 'Limpar':
        window['-OUTPUT-'].update('')

window.close()
