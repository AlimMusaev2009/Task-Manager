"""подтверждение действия"""
import sys
import os

def check_confirm(action: str):
    confirm = input("точно? (Y/N): ").strip().lower()  
    yes_variants = ['y', 'yes', 'да', 'д']
    
    if confirm in yes_variants:
        print(action)
        return True  # Подтверждено
    else:
        print("отмена")
        return False  # Отменено

def get_base_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))

def insure_save_file(name_file: str):
    if not os.path.exists(name_file):
        with open(name_file, "w") as f:
            f.write("")
