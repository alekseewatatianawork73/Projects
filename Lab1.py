# подключаем все необходимые библиотеки
import customtkinter as ctk
from random import randint
from pygame import mixer
mixer.init()

start_count = 10  # исходное количество попыток
count = 10  # текущее количество попыток

# устанавливаем диапазон загадываемых чисел
start = 1
finish = 100
digit = randint(start, finish)  # загаданное число

# переменная для текстовой метки рядом со слайдером CtkSlider() для обозначения количества попыток
# (сделали её глобальной, чтобы использовать в нескольких функциях)
value_count = None

audio = False  # переменная для звука(вкл/выкл)
mixer.music.load('audio.mp3')  # загружаем mp3-файл со звуком

# создаём главное окно
root = ctk.CTk()
root.title('Игра "Угадай число"')
root.geometry("1000x700")
root.configure(fg_color='misty rose')

# задаём основной шрифт
my_font = ctk.CTkFont(family='Arial', size=20, weight='bold')


# функция-обработчик для кнопки Угадать число
def press_frm(k):
    global count, digit, start_count
    count -= 1
    lbl2.configure(text=f'У вас осталось {count} попыток.')
    if k != digit and count > 0:
        s = 'побольше' if digit > k else 'поменьше'
        lbl_res.configure(text=f'Вы не угадали. Введите число {s}')
    else:
        txt_output.grid_forget()
        btn_frm.grid_forget()
        if k == digit:
            lbl_res.configure(text=f'Вы выиграли! Ваш счёт: {start_count - count}')
        else:
            lbl_res.configure(text='Вы проиграли!')


# функция-обработчик для кнопки Применить (изменяет диапазон загадываемых чисел)
def span(a, b):
    global start, finish, digit
    start, finish = int(a), int(b)
    lbl1.configure(text=f'Угадайте число от {start} до {finish}.')


# функция-обработчик для переключателя звука
def sw_comm(val, sw):
    global audio
    audio = val
    if val:
        sw.configure(text='on')
        mixer.music.play(-1)
    else:
        sw.configure(text='off')
        mixer.music.stop()


# функция-обработчик для слайдера (изменяет количество попыток)
def cnt(value):
    global count, start_count
    count = round(value)
    start_count = count
    value_count.configure(text=f'{count}')
    lbl2.configure(text=f'У вас осталось {count} попыток.')


# функция-обработчик для кнопки Начать заново
def press1():
    global digit, count, start_count
    digit = randint(start, finish)
    new_game.grid(row=1, rowspan=3, column=2, columnspan=3, padx=20, pady=20, sticky="nsew")
    txt_output.grid(row=2, column=3, padx=10, pady=10, sticky='ns')
    btn_frm.grid(row=3, column=3, padx=20, pady=20, sticky="nsew")
    lbl_res.configure(text='')
    count = start_count
    lbl2.configure(text=f'У вас осталось {count} попыток.')
    root.after(3000, lambda: new_game.grid_forget())


# функция-обработчик для кнопки Параметры игры
def press2():
    global start, finish, count
    window = ctk.CTkToplevel()
    window.title('Параметры')
    window.geometry('1000x500')
    window.configure(fg_color='lightyellow')
    r, c = 7, 7
    for i in range(r):
        window.rowconfigure(index=i, weight=1)
    for i in range(c):
        window.columnconfigure(index=i, weight=1)

    # изменяем диапазон загадываемых чисел
    lbl11 = ctk.CTkLabel(master=window)
    lbl11.configure(text='Изменить диапазон загадываемых чисел:', font=my_font)
    lbl11.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
    entry_from = ctk.CTkEntry(master=window)
    entry_from.configure(justify='center', border_width=2, border_color='yellow4', font=my_font, placeholder_text='От')
    entry_from.grid(row=0, column=1, padx=20, pady=20, sticky="ew")
    entry_to = ctk.CTkEntry(master=window)
    entry_to.configure(justify='center', border_width=2, border_color='yellow4', font=my_font, placeholder_text='До')
    entry_to.grid(row=0, column=2, padx=20, pady=20, sticky="ew")
    btn_span = ctk.CTkButton(master=window)
    btn_span.configure(text="Применить", fg_color='yellow', hover_color='lightgrey', font=my_font, text_color='black',
                       border_color='yellow4', border_width=2, command=lambda: span(entry_from.get(), entry_to.get()))
    btn_span.grid(row=0, column=3, padx=10, pady=10, sticky="ew")

    # изменяем количество доступных попыток
    lbl22 = ctk.CTkLabel(master=window)
    lbl22.configure(text='Изменить количество доступных попыток:', font=my_font)
    lbl22.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
    global value_count, audio
    value_count = ctk.CTkLabel(master=window)
    value_count.configure(text=f'{count}', font=my_font)
    value_count.grid(row=1, column=3, padx=10, pady=10, sticky="ew")
    count_slider = ctk.CTkSlider(master=window)
    count_slider.configure(from_=1, to=50, number_of_steps=50, fg_color='yellow', button_color='yellow4',
                           progress_color='yellow3', button_hover_color='lightgrey', command=cnt)
    count_slider.grid(row=1, column=1, columnspan=2, padx=20, pady=20, sticky="ew")

    # настройки фонового звука
    lbl33 = ctk.CTkLabel(master=window)
    lbl33.configure(text='Звуковые эффекты (вкл/выкл):', font=my_font)
    lbl33.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
    sw = ctk.CTkSwitch(master=window)
    sw_var = ctk.BooleanVar(value=audio)
    sw.configure(text='on' if audio else 'off', variable=sw_var, font=my_font, command=lambda: sw_comm(sw_var.get(), sw),
                 fg_color='yellow', button_color='yellow4', progress_color='yellow3', button_hover_color='lightgrey')
    sw.grid(row=2, column=1, padx=10, pady=10, sticky="ew")


frm = ctk.CTkFrame(master=root, width=200, height=200)
frm.configure(fg_color='lightyellow', border_color='yellow4', border_width=3)
frm.grid(row=1, rowspan=3, column=2, columnspan=3, padx=20, pady=20, sticky="nsew")

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
    frm.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)
    frm.columnconfigure(index=i, weight=1)

start_frm = ctk.CTkFrame(master=root, width=200, height=200)
start_frm.configure(fg_color='lightcoral')
start_frm.grid(row=0, column=3, padx=20, pady=20, sticky="ew")
start_frm.rowconfigure(index=0, weight=1)
start_frm.columnconfigure(index=0, weight=1)

start_lbl = ctk.CTkLabel(master=start_frm)
start_lbl.configure(text='Игра «Угадай число»', font=ctk.CTkFont(family='Arial', size=30, weight='bold'))
start_lbl.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

new_game = ctk.CTkLabel(master=root)
new_game.configure(text=f'Загадано новое число!', font=my_font)

lbl1 = ctk.CTkLabel(master=frm)
lbl1.configure(text=f'Угадайте число от {start} до {finish}.', font=my_font)
lbl1.grid(row=1, column=3, padx=10, pady=10, sticky='nsew')

lbl2 = ctk.CTkLabel(master=frm)
lbl2.configure(text=f'У вас осталось {count} попыток.', font=my_font)
lbl2.grid(row=5, column=3, padx=10, pady=10, sticky='nsew')

lbl_res = ctk.CTkLabel(master=frm)
lbl_res.configure(text='', font=my_font)
lbl_res.grid(row=4, column=3, padx=10, pady=10, sticky='ew')

txt_output = ctk.CTkEntry(master=frm)
txt_output.configure(justify='center', font=my_font, fg_color='white', border_color='yellow4', border_width=2)
txt_output.grid(row=2, column=3, padx=10, pady=10, sticky='ns')

btn_frm = ctk.CTkButton(master=frm)
btn_frm.configure(text="Угадать число", fg_color='yellow', hover_color='lightyellow', text_color='black',
                  font=ctk.CTkFont(family='Arial', size=15, weight='bold'), border_color='yellow4',
                  border_width=2, command=lambda: press_frm(int(txt_output.get())))
btn_frm.grid(row=3, column=3, padx=20, pady=20, sticky="nsew")

btn1 = ctk.CTkButton(master=root)
btn1.configure(text="Начать заново", fg_color='lightcoral', hover_color='lightpink', font=my_font, text_color='black',
               border_color='darkred', border_width=2, command=press1)
btn1.grid(row=4, column=3, padx=20, pady=20, sticky="nsew")
btn2 = ctk.CTkButton(master=root)
btn2.configure(text="Параметры игры", fg_color='lightcoral', hover_color='lightpink', font=my_font, border_color='darkred',
                  border_width=2, text_color='black', command=press2)
btn2.grid(row=5, column=3, padx=20, pady=20, sticky="nsew")
btn3 = ctk.CTkButton(master=root)
btn3.configure(text="Завершить игру", fg_color='lightcoral', hover_color='lightpink', font=my_font, text_color='black',
               border_color='darkred', border_width=2, command=root.destroy)
btn3.grid(row=6, column=3, padx=20, pady=20, sticky="nsew")

root.mainloop()
