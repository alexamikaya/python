# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 14:04:30 2022

@author: user
"""

from tkinter import *
from tkinter import messagebox


import step_1_add_product as s2
import step_2_show_all as s3
import step_4_find_category as s5
import step_5_sort as s6
import step_6_delete_all as s7
def add():
    data = s2.add_new()
    var.set(str(data))
def show():
    data = s3.update_show_all()
    var.set(str(data))
def sort():
    data = s6.sort()
    var.set(str(data))
def find():
    data = s5.find_category()
    var.set(str(data))
def delete():
    data = s7.delete()
    var.set(str(data))
    
window = Tk()
window.title("Calculation")
window.geometry("300x250")
hello = "Hello!"
lbl = Label(window, text=hello, font=("Arial Bold", 20))  
lbl.grid(column=0, row=0)  
mainmenu = Menu(window)
window.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Add", command=add)
filemenu.add_command(label="Show all", command=show)
filemenu.add_command(label="Show by category", command=find)
filemenu.add_command(label="Show by min->max", command=sort)
filemenu.add_command(label="Delete", command=delete)
filemenu.add_command(label="Exit", command=window.destroy)

mainmenu.add_cascade(label="File", menu=filemenu)


window.mainloop()