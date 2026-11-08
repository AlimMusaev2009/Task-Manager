"""
==============================
    модуль с функциями сохранения и загрузки
==============================
"""
import json
import os
from config import FILE_NAME_SAVES


def load_collection():
    file_exists = os.path.exists(FILE_NAME_SAVES)

    if file_exists == False:
        return []

    file = open(FILE_NAME_SAVES, "r", encoding="utf-8")
    data = json.load(file)
    file.close()

    return data


def save_collection(task_list):
    file = open(FILE_NAME_SAVES, "w", encoding="utf-8")

    json.dump(task_list, file, ensure_ascii=False, indent=4)

    file.close()
