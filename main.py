from tkinter import *
import tkinter as ttk
import service

class Gallows:
    def __init__(self):
        self.init_game()

    def init_game(self):
        self.root = Tk()
        self.root.geometry('1000x500')
        self.root.title('Виселица')

        self.button1 = ttk.Button(self.root,text='Начать', command=self.show_word)
        self.button1.pack()

        self.label = ttk.Label(self.root)
        self.label.pack()

        self.entry = ttk.Entry()
        self.entry.pack()

        self.health_points = ['*', '*', '*']

        self.root.mainloop()

    def check_word(self, word):
        # Проверить на совпадение слово из word и self.generated_word
        # Если все правильно, выводим в label, где HP, что пользователь выиграл
        # Если неправильно, отнимаем жизнь self.health_points.pop(), обновляем label с HP.
        # word.lower() и self.generated_word.lower()

        print(word.lower(), self.generated_word.lower())

        if word.lower() == self.generated_word.lower():
            self.healthpoints_label.config(text='Поздравляем, Вы выиграли!')
        else:
            try:
                self.health_points.pop()
                self.healthpoints_label.config(text=self.health_points)
                self.label.config(text=self.generated_tip[self.counter])
                self.counter += 1
            except IndexError:
                self.healthpoints_label.config(text='Вы проиграли! У вас закончились жизни.')
                self.check_button.config(state="disable")
                self.button1.config(state="disable")

        
    def show_word(self):
        if self.label.cget("text") == "":
            self.counter = 0

            self.generated_pair = service.random_word()

            self.generated_word = self.generated_pair[0]
            self.generated_tip = self.generated_pair[1]     

            self.label.config(text=self.generated_tip[self.counter])
            self.counter += 1

            self.healthpoints_label = ttk.Label(self.root)
            self.healthpoints_label.config(text=self.health_points)
            
            self.check_button = ttk.Button(self.root, text='Проверить', command=lambda: self.check_word(self.entry.get()))
            self.check_button.pack()

            self.healthpoints_label.pack()



gallows = Gallows()