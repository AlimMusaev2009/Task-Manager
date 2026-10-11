""" Приложение Task Manager
    =============================================================
        консольное приложение - менеджер управления заметок,
        пользователь может создать заметку, редактировать,
        посмотреть все заметки или удалить выбранную.
    =============================================================
    ~~~~~~~~~~~~~~~~~~~~~
    | version app 0.0.7 |
    ~~~~~~~~~~~~~~~~~~~~~

    v(0.0.1)
    разработан цикл приложения - структурное программирование

    v(0.0.2)
    внедрен i/o функционал для ввода задачи

    v(0.0.3)
    разработаны функции для цикла - функциональное программирование

    v(0.0.4)
    добавлены проверки и подтверждения

    v(0.0.5)
    созданы методы сохранения и загрузки - файловые сохранения

    v(0.0.6)
    созданы методы для удаления, редактирования и создания задач - логика вынесена из цикла

    v(0.0.7)
    основной цикл помещен в отдельный метод - def main

    v(0.0.8)
    реализован функционал добавления контента задачи - имя + содержание

    v(0.0.9)

"""

"""основной цикл"""

from viev import show_collection, show_message
from utils import *
from core import create_task, edited_task, deleated_task
from loader import load_collection, save_collection
import os.path

def main():
    name_file = os.path.join(get_base_dir() ,"saves.txt")
    collection = load_collection([], name_file)
    insure_save_file(name_file)
    is_running = True

    while is_running:
        print('1 - посмотреть задачи'
              '\n2 - добавить задачу'
              '\n3 - редактирование'
              '\n4 - снять задачу'
              '\n5 - выход')
        choice_user: str = input("введите команду: ")

        match str(choice_user):
            case "1":  # просмотр списка
                show_collection(collection)
            case "2":  # добавление в список
                create_task(collection, name_file)
            case "3":  # изменение элемента
                edited_task(collection)
                save_collection(collection, name_file)
            case "4":  # удаление элемента
                show_collection(collection)
                deleated_task(collection)
                save_collection(collection, name_file)
            case "5":  # завершение цикла
                is_running = check_confirm('отключение...')
            case _:  # неверная команда
                print('неверная команда')
                show_message()



