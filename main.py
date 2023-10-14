from tkinter import *
import tkinter as ttk
import service
import random

class Gallows:
    def __init__(self):
        self.init_game()
        self.health_points = ['*', '*', '*']

    def init_game(self):
        self.root = Tk()
        self.root.geometry('1000x500')
        self.root.title('Виселица')


        self.button1 = ttk.Button(self.root,text='Начать', command=self.show_word)
        self.button1.pack()

        self.label = ttk.Label(self.root)
        self.label.pack()

        

        self.root.mainloop()

        self.entry = ttk.Entry()
        self.entry.pack()

    def show_word(self):
        counter = 0

        generated_word = service.random_word()[1][counter]
        counter += 1

        self.label.config(text=generated_word)
        

gallows = Gallows()