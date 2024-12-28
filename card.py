from tkinter import *
from tkinter import ttk
import random
import time
from db import DB
from graf import Graph
from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME, 'ru')
today = datetime.today()
month = today.month
mydate= str(month)
month = datetime.strptime(mydate, "%m").strftime("%B")


class Interface():
    def set_up(self,title,size):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(size)
        self.font = ("Times New Roman",15)
        self.database = DB()
        self.database.set_up()
        self.interface()
        self.root.mainloop()

    def interface(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(pady=10,expand=True)
        word_label = ttk.Frame(notebook)
        notebook.add(word_label,text="Слова")
        Label(word_label,text="Введите слово ",font=self.font).pack(ipady=5)
        self.original_word = StringVar()
        Entry(word_label,textvariable=self.original_word,width=50,font=self.font).pack(ipady=5)
        Label(word_label,text="Введите перевод",font=self.font).pack(ipady=5)
        self.translated_word_entry = StringVar()
        Entry(word_label,textvariable=self.translated_word_entry,font=self.font,width=50).pack(ipady=5)
        Button(word_label,text="Подтвердить",foreground="white",command=self.get_informations,border="0",background="green").pack(ipady=5)
        self.error_label = StringVar()
        Label(word_label,textvariable=self.error_label,font=self.font,foreground="red").pack(ipady=5)
        self.success_label = StringVar()
        Label(word_label,textvariable=self.success_label,font=self.font).pack(ipady=5)
        Button(word_label,text="Показать все слова",command=self.show_words,border="0",background="green",foreground="white").pack(ipady=5)
        self.text = Text(word_label)
        Button(word_label,text="Показать график",foreground="white",background="green",command=self.show_graph).pack(side="bottom")
        self.exercise_word = ttk.Frame(notebook)
        notebook.add(self.exercise_word,text="Тренировка")
        Button(self.exercise_word,text="Начать тренировку",foreground="white",background="green",font=self.font,border="0",command=self.random_exercise).pack(ipady=2)
        self.variable = StringVar()
        self.label = Label(self.exercise_word,textvariable=self.variable)
        self.true_string = StringVar()
        self.random_one = StringVar()
        self.random_two = StringVar()
        self.answer = StringVar(value=self.random_two)
        self.radio_button_one = Radiobutton(self.exercise_word,textvariable=self.true_string,value=1,variable=self.answer)
        self.radio_button_second = Radiobutton(self.exercise_word,textvariable=self.random_one,value=2,variable=self.answer)
        self.radio_button_third = Radiobutton(self.exercise_word,textvariable=self.random_two,value=3,variable=self.answer)
        Button(self.exercise_word,text="Подтвердить",foreground="white",background="green",command=self.confirm_values).pack(side="bottom")
        self.success = StringVar()
        self.error = StringVar()
        Label(self.exercise_word,textvariable=self.success,foreground="green",font=self.font).pack(side="bottom")
        Label(self.exercise_word,textvariable=self.error,foreground="red",font=self.font).pack(side="bottom")
    def get_informations(self):
        english_word = self.original_word.get()
        translated_word = self.translated_word_entry.get()
        if not english_word or not translated_word:
            self.success_label.set("")
            self.error_label.set("Вы должны заполнить все пункты")
        else:
            self.original_word.set("")
            self.translated_word_entry.set("")
            self.success_label.set("Вы успешно добавили слово в базу данных")
            self.database.add_to_db(english_word,translated_word,month)
            self.error_label.set("")

    def show_words(self):
        all_informations = self.database.show_words()
        self.text.pack(pady=5)
        self.text.delete("1.0",END)
        self.text.insert(END,all_informations)


    def random_exercise(self):
        randoms = self.database.give_random()
        true_key = randoms[0]
        self.true_values = randoms[1]
        random_one = randoms[2][0]
        random_second = randoms[2][1]
        self.label.forget()
        self.label.pack(ipady=5)
        self.variable.set(true_key)
        self.radio_button_one.forget()
        self.radio_button_one.pack(side="left")
        self.true_string.set(self.true_values)
        self.radio_button_second.forget()
        self.radio_button_second.pack(side="left")
        self.random_one.set(random_one)
        self.radio_button_third.forget()
        self.radio_button_third.pack(side="left")
        self.random_two.set(random_second)

    def confirm_values(self):
        answer = self.answer.get()
        true_value = "1"
        if answer == true_value:
            self.error.set("")
            self.success.set("Вы успешно угадали слово")
            time.sleep(0.5)
            self.random_exercise()
        else:
            self.success.set("")
            self.error.set("Вы не угадали слово")
            time.sleep(0.5)
            self.random_exercise()

    
    def show_graph(self):
        test = ["Декабрь","Январь","Февраль","Март"]
        something = self.database.get_for_graph(month)
        size = [len(something)]
        self.graph = Graph(test,size)
        self.graph.show()

tkinter = Interface()
tkinter.set_up("Flash-Cards","800x800")
