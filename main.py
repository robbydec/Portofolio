import PySimpleGUI as sg
import pandas as pd

sg.theme('Dark')

EXCEL_FILE = 'main.xlsx'
df = pd.read_excel(EXCEL_FILE)

layout = [
    [sg.Text('Input Pelanggan')],
    [sg.Input(key='Tanggal', size=(20,1)),
        sg.CalendarButton('Tanggal',
        close_when_date_chosen=True,  target='Tanggal',
        location=(0,0), no_titlebar=False, )],
    [sg.Text('Nama', size=(15,1)), sg.InputText(key='Nama')],
    [sg.Text('No. Hp/Tlp', size=(15,1)), sg.InputText(key='No. Hp/Tlp')],
    [sg.Text('Jumlah Barang', size=(15,1)), sg.InputText(key='Jumlah Barang')],
    [sg.Text('Harga', size=(15,1)), sg.InputText(key='Harga')],

    [sg.Submit(), sg.Exit()]
]
window = sg.Window("Data Pelanggan JNE", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit' :
        break
    if event == 'Submit':
        df = df.append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Data Tersimpan!')
window.close()
