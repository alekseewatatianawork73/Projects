import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np


def graph3d(f):
    fig = Figure(figsize=(7, 5))
    ax = fig.add_subplot(111, projection='3d')
    x = np.linspace(-10, 10, 500)
    y = x
    if f == 'sin':
        z = np.sin(x)
    elif f == 'cos':
        z = np.cos(x)
    elif f == 'tan':
        z = np.tan(x)
    else:
        z = int(f[0]) * x**2 + int(f[1]) * x + int(f[2])
    ax.plot(x, y, z, color='darkred')

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=3, padx=5, pady=5)


def graph2d(f):
    fig = Figure(figsize=(7, 5))
    ax = fig.add_subplot(111)
    x = np.linspace(-10, 10, 500)
    if f == 'sin':
        y = np.sin(x)
    elif f == 'cos':
        y = np.cos(x)
    elif f == 'tan':
        y = np.tan(x)
    else:
        y = int(f[0]) * x**2 + int(f[1]) * x + int(f[2])
    ax.plot(x, y, color='darkred')

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=3, padx=5, pady=5)



def om(choice):
    for widget in root.grid_slaves():
        if str(widget.grid_info()['row']) in '345':
            widget.grid_forget()
    if choice == 'Тригонометрические':
        btns = [ctk.CTkButton(master=root) for _ in range(6)]
        for btn in btns:
            btn.configure(font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
        btns[0].configure(text="sin 2D", command=lambda: graph2d('sin'))
        btns[0].grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
        btns[1].configure(text="cos 2D", command=lambda: graph2d('cos'))
        btns[1].grid(row=3, column=3, padx=5, pady=5, sticky="nsew")
        btns[2].configure(text="tg 2D", command=lambda: graph2d('tan'))
        btns[2].grid(row=3, column=4, padx=5, pady=5, sticky="nsew")
        btns[3].configure(text="sin 3D", command=lambda: graph3d('sin'))
        btns[3].grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
        btns[4].configure(text="cos 3D", command=lambda: graph3d('cos'))
        btns[4].grid(row=4, column=3, padx=5, pady=5, sticky="nsew")
        btns[5].configure(text="tg 3D", command=lambda: graph3d('tan'))
        btns[5].grid(row=4, column=4, padx=5, pady=5, sticky="nsew")
    elif choice == 'Квадратичные':
        lbl_square = ctk.CTkLabel(master=root)
        lbl_square.configure(text='Введите коэффициенты квадратного уравнения:', font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
        lbl_square.grid(row=3, column=3, padx=10, pady=10, sticky="ew")
        sq_entries = [ctk.CTkEntry(master=root) for _ in range(3)]
        for entr in sq_entries:
            entr.configure(font=ctk.CTkFont(family='Arial', size=15, weight='bold'))
        sq_entries[0].configure(placeholder_text='a')
        sq_entries[0].grid(row=4, column=2, padx=5, pady=5, sticky="ns")
        sq_entries[1].configure(placeholder_text='b')
        sq_entries[1].grid(row=4, column=3, padx=5, pady=5, sticky="ns")
        sq_entries[2].configure(placeholder_text='c')
        sq_entries[2].grid(row=4, column=4, padx=5, pady=5, sticky="ns")
        sq_btns = [ctk.CTkButton(master=root) for _ in range(2)]
        for btn in sq_btns:
            btn.configure(font=ctk.CTkFont(family='Arial', size=20, weight='bold'))
        sq_btns[0].configure(text="Отобразить 2D-график", command=lambda: graph2d([entr.get() for entr in sq_entries]))
        sq_btns[0].grid(row=5, column=2, padx=5, pady=5, sticky="nsew")
        sq_btns[1].configure(text="Отобразить 3D-график", command=lambda: graph3d([entr.get() for entr in sq_entries]))
        sq_btns[1].grid(row=5, column=4, padx=5, pady=5, sticky="nsew")


ctk.set_appearance_mode('light')
root = ctk.CTk()
root.title("Работа с графиками")
root.geometry("1200x900")

frame = ctk.CTkFrame(master=root)
frame.configure(width=500, height=500, fg_color='lightgrey', cursor='cross', border_width=3)
frame.grid(row=2, column=1, columnspan=5, padx=10, pady=10, sticky="nsew")

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)
    frame.columnconfigure(index=i, weight=1)

lbl = ctk.CTkLabel(master=root)
lbl.configure(text='Графики функций', font=ctk.CTkFont(family='Arial', size=35, weight='bold', slant='italic'))
lbl.grid(row=0, column=3, padx=10, pady=10, sticky="ew")

menu = ctk.CTkOptionMenu(master=root)
menu.configure(anchor='center', values=['Тригонометрические', 'Квадратичные'], font=ctk.CTkFont(family='Arial', size=25), command=om)
menu.set('Выберите вид функции:')
menu.grid(row=1, column=3, padx=20, pady=20, sticky="ew")

btn_exit = ctk.CTkButton(master=root)
btn_exit.configure(text="Завершить программу", corner_radius=50, font=ctk.CTkFont(family='Arial', size=30, weight='bold'), command=lambda: root.destroy())
btn_exit.grid(row=6, column=3, padx=5, pady=5, sticky="nsew")

root.mainloop()
