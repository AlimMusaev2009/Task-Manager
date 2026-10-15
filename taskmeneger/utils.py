"""подтверждение действия"""
import sys
import os

def check_confirm(action: str):
    confirm = input("точно?\n Y/N: ")
    if confirm.upper().startswith('Y') or confirm.upper().startswith('Д'):
        print(action)
        return False  # Возвращаем False, чтобы цикл продолжился (или True, в зависимости от логики)
    else:
        print("отмена")
        return True

def get_base_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))

def insure_save_file(name_file):
    if not os.path.exists(name_file):
        with open(name_file, "w") as f:
            f.write("")