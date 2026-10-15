import tkinter as tk

score = 0

def on_click():
    global score
    score += 1
    score_label.config(text=f"Очки: {score}")

root = tk.Tk()
root.title("Простой Кликер")
root.geometry("300x250")

score_label = tk.Label(root, text="Очки: 0", font=("Arial", 20, "bold"))
score_label.pack(pady=30)

click_button = tk.Button(
    root,
    text="Кликни меня!",
    font=("Arial", 14),
    width=15,
    height=2,
    bg="lightblue",
    command=on_click
)
click_button.pack(pady=20)

root.mainloop()