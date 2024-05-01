import customtkinter as ctk

# функция добавления записи в основное окно
def addquestion(task):
    new_task = ctk.CTkFrame(master=root) # для записи новой задачи создаём фрейм (рамку), чтобы запись красиво отображалась
    # заполняем фрейм
    check_box = ctk.CTkCheckBox(master=new_task, text=task, font=ctk.CTkFont(family="Arial", size=15)) # создаём в рамке чекбокс (список с галочками)
    check_box.pack(anchor="nw", side="left")  # расплагаем запись слева и сверху
    but = ctk.CTkButton(master=new_task, text="Удалить", command=lambda: new_task.pack_forget()) # кнопка для удаления дела
    but.pack(anchor="nw", side="left")  # расплагаем кнопку слева и сверху
    new_task.pack(anchor="nw", padx=5, pady=5) # располагаем фрейм (рамку) слева и сверху с отступами


# окно для добавления новой записи
def newquestion():
    window = ctk.CTkToplevel(root)
    window.title("Добавить дело")
    window.geometry("500x150")
    entry_input = ctk.CTkEntry(master=window, width=250)
    entry_input.configure(justify="center")
    entry_input.pack(pady=5, padx=5)
    # кнопка для добавления записи в основное окно
    addquestion_res = ctk.CTkButton(master=window)
    addquestion_res.configure(text="Cохранить", command=lambda: addquestion(entry_input.get())) 
    addquestion_res.pack()



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
root = ctk.CTk()
root.title("Планировщик дел")
root.geometry("700x300")


lbl_start_message = ctk.CTkLabel(master=root)
lbl_start_message.configure(text="Список ваших дел", font=ctk.CTkFont(family="Arial", size=20))
lbl_start_message.pack()
btn_result = ctk.CTkButton(master=root)
btn_result.configure(text="Создать новую заметку", command=newquestion)
btn_result.pack(anchor="s", side="bottom") # располагаем кнопку снизу

root.mainloop()
