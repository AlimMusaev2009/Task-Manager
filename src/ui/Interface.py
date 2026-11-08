import tkinter as tk
from tkinter import messagebox
from .components.AppButton import AppButton
from .components.AppLabel import AppLabel
from src.storage import save_collection, load_collection


class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x600")
        self.root.title("Task Manager")
        self.root.configure(bg="black")
        self.task_lists = load_collection()

    def clear_window(self):
        all_widgets = self.root.winfo_children()
        for widget in all_widgets:
            widget.destroy()

    def show_menu(self):
        self.clear_window()

        AppLabel(self.root, "Главное меню", "title")

        btn_show = AppButton(self.root, "primary", "Показать задачи", self.show_tasks)
        btn_show.pack(pady=10)

        btn_add = AppButton(self.root, "secondary", "Добавить задачу", self.show_add_form)
        btn_add.pack(pady=10)

        btn_exit = AppButton(self.root, "exit", "Выход", self.root.quit)
        btn_exit.pack(pady=10)

    def show_tasks(self):
        self.clear_window()

        AppLabel(self.root, "Список задач:", "title")

        listbox = tk.Listbox(self.root, width=50, height=15)
        listbox.pack(pady=10)

        for task in self.task_lists:
            task_name = task["name"]
            task_content = task["content"]
            text_for_list = task_name + " | " + task_content
            listbox.insert(tk.END, text_for_list)

        btn_back = AppButton(self.root, "exit", "Назад", self.show_menu)
        btn_back.pack(pady=10)

    def show_add_form(self):
        self.clear_window()

        AppLabel(self.root, "Новая задача", "title")

        AppLabel(self.root, "Название задачи:")
        self.entry_name = tk.Entry(self.root, width=40)
        self.entry_name.pack(pady=5)

        AppLabel(self.root, "Описание задачи:")
        self.entry_content = tk.Entry(self.root, width=40)
        self.entry_content.pack(pady=5)

        btn_save = AppButton(self.root, "primary", "Сохранить", self.add_task)
        btn_save.pack(pady=20)

        btn_back = AppButton(self.root, "exit", "Назад", self.show_menu)
        btn_back.pack(pady=5)

    def add_task(self):
        name = self.entry_name.get()
        content = self.entry_content.get()

        name = name.strip()
        content = content.strip()

        if len(name) == 0:
            messagebox.showwarning("Ошибка", "Название не может быть пустым!")
            return

        new_task = {}
        new_task["name"] = name
        new_task["content"] = content
        new_task["author"] = "User"

        self.task_lists.append(new_task)
        save_collection(self.task_lists)
        self.show_tasks()
