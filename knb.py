from customtkinter import *
from tkinter import *
import random

COUNT_USER = 0  # наш счёт
COUNT_COMP = 0  # счёт соперника (компьютера)

# функция для отображения счёта
def clicked():
    lbl.configure(text=f'Ваши баллы: {COUNT_USER}, Баллы соперника: {COUNT_COMP}.')   # заменяем "Привет! Начнём игру!" на результат (используем f-строку)

  # проверяем, выиграли мы или проиграли
    if COUNT_USER > COUNT_COMP:
        lbl_rez.configure(text="Вы выиграли!")
    elif COUNT_USER < COUNT_COMP:
        lbl_rez.configure(text="Вы проиграли!")
    else:
        lbl_rez.configure(text="Ничья!")
      
    finish_message.configure(text="Закройте окно, чтобы начать игру заново.")


# обработка кнопки "камень"
def kmn():
    comp = random.choice(["Камень", "Ножницы", "Бумага"])

  # увеличиваем наш счёт или счёт соперника
    global COUNT_USER, COUNT_COMP
    if comp == "Ножницы":
        COUNT_USER += 1
    elif comp == "Бумага":
        COUNT_COMP += 1

  # записываем в поле ввода наш выбор
    input.configure(state="normal")   # делаем поле изменяемым, чтобы вписать текст
    input.delete(0, "end")            # очищаем предыдущий текст
    input.insert(0, "Камень")         # вписываем наш выбор, всталяем в начало (на позицию 0)
    input.configure(state="readonly") # снова делаем поле неизменяемым (только для чтения)

  # записываем в поле вывода результат соперника
    output.configure(state="normal")   # делаем поле изменяемым, чтобы вписать текст
    output.delete(0, "end")            # очищаем предыдущий текст
    output.insert(0, comp)             # вписываем выбор компьютера (соперника), всталяем в начало (на позицию 0)
    output.configure(state="readonly") # снова делаем поле неизменяемым (только для чтения)

# обработка кнопки "ножницы"
def njn():
    pass  # аналогично функции для кнопки "камень"

# обработка кнопки "бумага"
def bmg():
    pass  # аналогично функции для кнопки "камень"

# основная программа
window = Tk()
window.geometry('1000x500')
window.title("Добро пожаловать в 'Камень, ножницы, бумага' ")

# рисуем сетку 7x7, чтобы размещать элементы
rows, columns = 7, 7
for i in range(rows):
    window.rowconfigure(index=i, weight=1)
for i in range(columns):
    window.columnconfigure(index=i, weight=1)

# Начальная текстовая метка
lbl = Label(window, text="Привет! Начнём игру!", font=("Times New Roman", 30))

# текстовые метки для полей, где отображается наш выбор и выбор соперника
lbl_input = Label(window, text="Ваш выбор:", font=("Times New Roman", 20))
lbl_output = Label(window, text="Выбор соперника:", font=("Times New Roman", 20))

lbl.grid(column=1, row=0, columnspan=3)
lbl_input.grid(column=1, row=1, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
lbl_output.grid(column=3, row=1, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")


input = Entry(master=window)  # поле, где отображается наш выбор
output = Entry(master=window) # поле, где отображается выбор соперника
input.configure(justify='center', state='readonly', font=("Times New Roman", 20))
output.configure(justify='center', state='readonly', font=("Times New Roman", 20))
input.grid(column=1, row=2, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
output.grid(column=3, row=2, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")

# кнопки
kam = Button(window, text="Камень", font=("Times New Roman", 20), command=kmn)
kam.grid(column=1, row=3)
nozh = Button(window, text="Ножницы", font=("Times New Roman", 20), command=njn)
nozh.grid(column=2, row=3)
bum = Button(window, text="Бумага", font=("Times New Roman", 20), command=bmg)
bum.grid(column=3, row=3)
schet = Button(window, text="Счет", font=("Times New Roman", 20), command=clicked)
schet.grid(column=2, row=4)

# текстовая метка с результатом игры (при нажатии кнопки счёт)
lbl_rez = Label(window, font=("Times New Roman", 50))
lbl_rez.grid(column=2, row=5)

# текстовая метка, которая отображается после завершения игры (при нажатии кнопки "счёт")
finish_message = Label(window, font=("Times New Roman", 20))
finish_message.grid(column=1, row=6, columnspan=3)

window.mainloop()
