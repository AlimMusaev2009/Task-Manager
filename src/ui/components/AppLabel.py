import tkinter as tk


class AppLabel(tk.Label):
    def __init__(self, master, text, status="normal"):
        super().__init__(master, text=text)

        if status == "title":
            self.configure(font=("Arial", 16, "bold"), bg="black", fg="white")
        elif status == "subtitle":
            self.configure(font=("Arial", 12), bg="black", fg="gray")
        else:
            self.configure(font=("Arial", 10), bg="black", fg="white")

        self.pack(pady=5, padx=10, anchor="w")