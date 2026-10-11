"""подтверждение действия"""
import sys
import os

def check_confirm(action: str):
    confirm = input("точно?"
                    "\n Y/N")
    if (confirm.capitalize().startswith('') == "Y"
            or 'Д'):
        print(action)
        return False
    else:
        print("отмена")
        return True

def get_base_dir():
    if getattr(sys, 'frozen', False):
        os.path.dirname(sys.executable)
    else:
        os.path.dirname(os.path.abspath(__file__))

def insure_save_file(name_file):
    if not os.path.exists(name_file):
        with open(name_file, "w") as f:
            f.write("")