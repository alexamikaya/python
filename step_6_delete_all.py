import pandas as df 
import tkinter.messagebox as mb
import tkinter as tk
from tkinter import ttk
import csv
def delete():
   
    
    window=tk.Tk()
    window.title('Calculation')
    frame_add_form = tk.Frame(window)
    frame_add_form.grid(column=0,row=0,sticky='ns')
    filename = "shop1.csv"
    shoplist = open(filename, "w")
    shoplist.truncate()
    shoplist.close()
    with open("shop1.csv", mode="a", encoding='utf-8', newline='') as file:
        w = csv.writer(file)
        w.writerow(['category', 'product', 'cost', 'date'])
   
    msg = "Поздравляем! Вы очистили ваши траты"
    mb.showinfo("Успех", msg)
