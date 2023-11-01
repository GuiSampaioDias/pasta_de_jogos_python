import requests
from tkinter import *

def pegar_cotacoes():
    url = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,CNY-BRL")

    dici = url.json()

    cotacao_dolar = dici['USDBRL']['bid']
    cotacao_euro  = dici['EURBRL']['bid']
    cotacao_btc   = dici['BTCBRL']['bid']
    cotacao_yuan  = dici['CNYBRL']['bid']

    cotacoes = f'''
    Dólar: {cotacao_dolar}
    Euro:  {cotacao_euro}
    BTC:   {cotacao_btc}
    RMB:   {cotacao_yuan}'''
    
    txt_rates["text"] = cotacoes

#pegar_cotacoes()

# fist steep creat a window before the rest

window = Tk() #TK() creat the window
window.title("Current Currency Rates") # window head text 

orientation_txt = Label(window, text="Click to get the current currency rates") # criate txt to put inside of the window
orientation_txt.grid(column = 0, row = 0) # indicates where the text will be placed

button = Button(window, text = 'Search Rates', command = pegar_cotacoes ) # button creattion
button.grid(column = 0, row = 1) # Replace the button in the label

txt_rates = Label(window, text = "")
txt_rates.grid(column = 0, row = 2)

window.mainloop() # end with mainloop()