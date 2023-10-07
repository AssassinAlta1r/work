from tkinter import *
import tkinter as ttk
import service

#print(service.random_word())

def show_message():

    
root = Tk()
root.geometry('1000x500')
root.title('Виселица')


button1 = ttk.Button(root,text='Начать')
button1.pack()
button2 = ttk.Button(root,text='Жми', command = show_message)
button2.pack


entry = ttk.Entry()
entry.pack(expand=TRUE)


label = ttk.Label(root)
label.place()
label.pack()


root.mainloop()