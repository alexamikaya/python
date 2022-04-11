
from tkinter import *
import pandas as pd 
    
import tkinter as tk

import csv
def find_category():
    
    window=tk.Tk()
    window.title('Calculation')
    frame_add_form = tk.Frame(window)
    frame_add_form.grid(column=0,row=0,sticky='ns')
    def show():
        
        window=tk.Tk()
        window.title('Calculation')
        width = 500
        height = 400
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        window.geometry("%dx%d+%d+%d" % (width, height, x, y))
        window.resizable(0, 0)
        TableMargin = Frame(window, width=500)
        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=("category", "product", "cost", "date"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('category', text="category", anchor=W)
        tree.heading('product', text="product", anchor=W)
        tree.heading('cost', text="cost", anchor=W)
        tree.heading('date', text="date", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=100)
        tree.column('#2', stretch=NO, minwidth=0, width=100)
        tree.column('#3', stretch=NO, minwidth=0, width=100)
        tree.column('#4', stretch=NO, minwidth=0, width=100)
        tree.pack()
        with open('shop1.csv') as f:
           
           read=pd.read_csv(f, delimiter=',', names=["category", "product", "cost", "date"]) 
           
           for row in read[read['category']== str(f_category.get())].itertuples():
               
               
               tree.insert("", 0, values=(row.category, row.product, row.cost, row.date))

    l_category = ttk.Label(frame_add_form, text = "What's the category?")
    f_category = ttk.Entry(frame_add_form, text = "Write category?")
    btn_submit= ttk.Button(frame_add_form, text = "Show", command = show)
    l_category.grid(row=0, column=0, sticky='w', padx=10, pady=10)
    f_category.grid(row=0, column=1, sticky='e', padx=10, pady=10)
    btn_submit.grid(row=4, column=1, columnspan=2, sticky='n',padx=10, pady=10)