# модуль visual.py создаёт графический интерфейс, logic.py - отвечает нахождение ответа

import logic  # подключаем модуль logic с функциями нахождения ответа

import customtkinter as ctk  # подключаем модуль customtkinter


def handle_pressing_btn_result():  # функция-обработчик события нажатия кнопки btn_result
    input_data = entry_input.get()  # получаем данные из поля ввода entry_input (в типе данных str)
    output_data = 0
    if cmbbox_operations.get() == "Операция 1: периметр квадрата":
        output_data = logic.op_1(input_data)  # высчитываем ответ, вызывая функцию op_1 из модуля logic
    elif cmbbox_operations.get() == "Операция 2: площадь квадрата":
        output_data = logic.op_2(input_data)  # аналогично - op_2
    entry_output.configure(state="normal")  # чтобы записать ответ в поле, необходимо сделать его снова активным
    entry_output.delete(0, "end")  # удаляем предыдущее значение
    entry_output.insert(0, output_data)  # вставляем новое значение
    entry_output.configure(state="readonly")  # снова делаем доступным только для чтения


# задаём цветовое оформление всего приложения
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()  # создаём главное окно
root.title("Поиск площади и периметра квадрата")  # устанавливаем название окна
root.geometry("1000x500")  # задаём размеры окна

# создаём виджеты
# текстовое поле для начального сообщения
lbl_start_message = ctk.CTkLabel(master=root)  # root - главное окно
# можно указывать св-ва при создании, а можно установить их отдельно в методе .configure()
lbl_start_message.configure(text="Выберите операцию из списка:")
# выпадающий список для выбора операции
operations = ["Операция 1: периметр квадрата", "Операция 2: площадь квадрата"]
cmbbox_operations = ctk.CTkComboBox(master=root)
cmbbox_operations.configure(justify="center", values=operations, state="readonly")
# justify - расположение по центру, state - только для чтения
cmbbox_operations.set("Операция 1: периметр квадрата")  # значение по умолчанию

# текстовые метки для обозначения окошек ввода и вывода
lbl_input, lbl_output = ctk.CTkLabel(master=root), ctk.CTkLabel(master=root)
lbl_input.configure(text="Сторона квадрата:")
lbl_output.configure(text="Результат:")
# поле для ввода
entry_input = ctk.CTkEntry(master=root)
entry_input.configure(justify="center")
# поле для вывода результата
entry_output = ctk.CTkEntry(master=root)
entry_output.configure(justify="center", state="readonly")
# кнопка получения результата
btn_result = ctk.CTkButton(master=root)
btn_result.configure(text="Получить результат", command=handle_pressing_btn_result)
# к кнопке с помощью параметра command привязываем функцию, которая будет обрабатывать нажатие

# для расположения виджетов на экране используем сетку - grid
rows, columns = 7, 7
# пусть будет сетка 7 x 7, каждой строке и столбцу установим вес 1, чтобы сетка была равномерной
# индексы строк и столбцов начинаются с нуля
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

# теперь расположим в ней наши виджеты
# виджет можно расположить в одной ячейке, например, в ячейке (0, 2), тогда укажем row=0, column=2
# а можно - в нескольких, например, в ячейках (0, 1) и (0, 2), тогда укажем: row=0, column=1, columnspan=2
# то есть columnspan растягивает виджет на 2 столбца
lbl_start_message.grid(row=0, column=3, columnspan=2, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
cmbbox_operations.grid(row=1, column=3, columnspan=2, sticky="ew")
lbl_input.grid(row=2, column=1, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
lbl_output.grid(row=2, column=5, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
entry_input.grid(row=3, column=1, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
entry_output.grid(row=3, column=5, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
btn_result.grid(row=4, column=3, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")

root.mainloop()
