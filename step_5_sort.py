from tkinter import *
import tkinter.ttk as ttk
import csv
import pandas as df 
def sort():
    
    root = Tk()
    root.title("Calculation")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)
    TableMargin = Frame(root, width=500)
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
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.column('#4', stretch=NO, minwidth=0, width=300)
    tree.pack()
    with open('shop1.csv') as f:
        
        reader = csv.DictReader(f, delimiter=',')
        sortedlist = sorted(reader, key=lambda row:int(row['cost']), reverse=True)
        
        for row in sortedlist:
            category = row['category']
            product = row['product']
            cost = row['cost']
            date = row['date']
            tree.insert("", 0, values=(category, product, cost, date))

    if __name__ == '__main__':
        root.mainloop()
