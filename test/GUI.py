import tkinter as tk
from tkinter import *
import datetime
import threading
from bs4 import BeautifulSoup
import datetime
import requests
import time
import lxml
from tkinter.font import Font

window = tk.Tk()
text = tk.Text(window)

get = requests.get('https://www.coinbase.com/price/bitcoin').content
soup = BeautifulSoup(get, "lxml")



def find_price():
    find1 = soup.find("div", {'class' : 'Flex-l69ttv-0 AssetChartAmount__Wrapper-sc-1b4douf-0 bIaMsv'} )
    label1.config(text=f"The price of BTC at {datetime.datetime.now().replace(microsecond=0)} is {find1.text}")
    find2=soup.find("div", {'class' : 'Flex-l69ttv-0 AssetChartHeader__PercentChangeContainer-sc-111iush-1 kfCArI'} )
    label2.config(text=f"The daily change in price of BTC at is {find2.text}")
    find3 = soup.find("span", {'class' : 'AssetStatDesktop__ValueText-sc-1dxbd6x-5 kLLcex'} )
    label3.config(text=f"The market cap of Bitcoin is {find3.text}")



def find_thread():
    threading.Thread(target=find_price).start()


def update():
    update.idle_tasks()

window.option_add('*Font', 'Arial')
window.title("BTC Price")
window.minsize(450, 80)
window.maxsize(450, 150)

PriceButton = Button(window, text="Bitcoin Price", command=lambda: [find_thread(), window.update_idletasks()])
PriceButton.place(x=0, y=0)
label1 = Label(window, bg="white")
label1.place(relx=0.5, rely=0.3, anchor='s')
label2 = Label(window, bg="white")
label2.place(relx=0.5, rely=0.45, anchor='s')
label3 = Label(window, bg="white")
label3.place(relx=0.5, rely=0.6, anchor='s')


label1.pack
label2.pack
label3.pack
PriceButton.pack
window.mainloop()
