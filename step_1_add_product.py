import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb
import csv
    
def add_new():
    
    filename = "shop1.csv"
    window=tk.Tk()
    window.title('Calculation')
    frame_add_form = tk.Frame(window)
    frame_add_form.grid(column=0,row=0,sticky='ns')
    
    def submit():
        
       
       
       with open("shop1.csv", mode="a", encoding='utf-8', newline='') as file:
           w = csv.writer(file)
           
           w.writerow([f_category.get(), f_product.get(), f_cost.get(), f_date.get()])
           
           msg = "Поздравляем! Ваши траты записаны"
           mb.showinfo("Успех", msg)               

        
    l_category = ttk.Label(frame_add_form, text = "What's the category?")
    f_category = ttk.Entry(frame_add_form, text = "Add category?")
    l_product = ttk.Label(frame_add_form, text = "What's the product?")
    f_product = ttk.Entry(frame_add_form, text = "Add product")
    l_cost = ttk.Label(frame_add_form, text = "What's the cost?")
    f_cost = ttk.Entry(frame_add_form, text = "Add cost")
    l_date = ttk.Label(frame_add_form, text = "Date: (dd/mm/yyyy)?")
    f_date = ttk.Entry(frame_add_form, text = "Add date?")
    btn_submit= ttk.Button(frame_add_form, text = "Submit", command = submit)
    
    l_category.grid(row=0, column=0, sticky='w', padx=10, pady=10)
    f_category.grid(row=0, column=1, sticky='e', padx=10, pady=10)
    l_product.grid(row=1, column=0, sticky='w', padx=10, pady=10)
    f_product.grid(row=1, column=1, sticky='e', padx=10, pady=10)
    l_cost.grid(row=2, column=0, sticky='w', padx=10, pady=10)
    f_cost.grid(row=2, column=1, sticky='e', padx=10, pady=10)
    l_date.grid(row=3, column=0, sticky='w', padx=10, pady=10)
    f_date.grid(row=3, column=1, sticky='e', padx=10, pady=10)
    btn_submit.grid(row=4, column=1, columnspan=2, sticky='n',padx=10, pady=10)
    
