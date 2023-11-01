import requests
from tkinter import *

def pegar_cotacoes(value):
    url = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,CNY-BRL")

    dici = url.json()

    cotacao_dolar = dici['USDBRL']['bid']
    cotacao_euro  = dici['EURBRL']['bid']
    cotacao_btc   = dici['BTCBRL']['bid']
    cotacao_yuan  = dici['CNYBRL']['bid']

    if value == 1:
        cotacoes = f'Dolar: {cotacao_dolar}'
    elif value == 2:
        cotacoes = f'Euro: {cotacao_euro}' 
    elif value == 3: 
        cotacoes = f'BTC: {cotacao_btc}'
    elif value == 4:
        cotacoes = f'RMB: {cotacao_yuan}'
    else:
        cotacoes = f'''Dólar: {cotacao_dolar}\nEuro:  {cotacao_euro}\nBTC:   {cotacao_btc}\nRMB:   {cotacao_yuan}'''
    
    txt_rates["text"] = cotacoes

#pegar_cotacoes()

# fist steep creat a window before the rest

window = Tk() #TK() creat the window
window.title("Current Currency Rates") # window head text 
window.geometry("280x200") # to open the window in a specific size

orientation_txt = Label(window, text="Chose wich rate you'd like to check") # criate txt to put inside of the window
orientation_txt.grid(column = 0, row = 0,padx = 10,pady = 10, columnspan = 5) # indicates where the text will be placed
                                                              #pady creat space axi x and axi y
button1 = Button(window, text = 'Dolar', command = lambda:pegar_cotacoes(1) ) # button creattion
button1.grid(column = 0, row = 1, padx = 10, pady = 10) # Replace the button in the label

button2 = Button(window, text = "Euro", command = lambda:pegar_cotacoes(2))
button2.grid(column = 1, row = 1, padx = 10, pady = 10)

butoon3 = Button(window, text = "BTC", command = lambda:pegar_cotacoes(3))
butoon3.grid(column = 2, row = 1, padx = 10, pady = 10)

button4 = Button(window, text = "RMB", command = lambda:pegar_cotacoes(4))
button4.grid(column = 3, row = 1, padx = 10, pady = 10)

button5 = Button(window, text = "ALL", command= lambda:pegar_cotacoes(5))
button5.grid(column = 4, row = 1, padx = 10, pady = 10)


txt_rates = Label(window, text = "")
txt_rates.grid(column = 0, row = 2, columnspan = 5, pady = 20)

window.mainloop() # end with mainloop()