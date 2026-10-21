from viev import show_collection, show_message
from utils import check_confirm
from loader import save_collection

"""создание задач"""

def create_task(task_list, file):
    name_task = input("введите имя задачи: ").strip()
    
    # Проверка на пустое имя и дубликаты
    if not name_task:
        print("Имя задачи не может быть пустым.")
        return
    
    # Проверяем, есть ли уже задача с таким именем
    existing_names = [task.split("|")[0] for task in task_list]
    if name_task in existing_names:
        print("Задача с таким именем уже существует.")
        return

    content_task = input("введите описание задачи: ").strip()
    
    # Объединяем через разделитель |
    full_task = f"{name_task}|{content_task}"
    task_list.append(full_task)
    save_collection(task_list, file_name=file)
    show_message(message=name_task, mess_action='добавлена')

"""изменение задачи"""

def edited_task(task_list):
    if not task_list:
        print("Список задач пуст.")
        return

    show_collection(task_list)
    try:
        select_edit = int(input('введите номер задачи: '))
    except ValueError:
        print("Ошибка: введите число.")
        return

    if select_edit < 1 or select_edit > len(task_list):
        print("Ошибка: задачи с таким номером не существует.")
        return

    # Разделяем старую задачу, чтобы сохранить описание, если пользователь не захочет его менять
    old_task_parts = task_list[select_edit - 1].split("|")
    
    edit_name = input("новое имя задачи (оставьте пустым, чтобы не менять): ").strip()
    if not edit_name:
        edit_name = old_task_parts[0]
        
    edit_content = input("новое описание (оставьте пустым, чтобы не менять): ").strip()
    if not edit_content:
        # Если описание было, сохраняем его
        edit_content = old_task_parts[1] if len(old_task_parts) > 1 else ""

    task_list[select_edit - 1] = f"{edit_name}|{edit_content}"
    show_message(message=edit_name, mess_action='изменена')

"""удаление элемента"""

def deleated_task(task_list):
    if not task_list:
        print("Список задач пуст.")
        return

    try:
        delete_edit = int(input('введите номер задачи для удаления: '))
    except ValueError:
        print("Ошибка: введите число.")
        return

    if delete_edit < 1 or delete_edit > len(task_list):
        print("Ошибка: задачи с таким номером не существует.")
        return

    # Удаляем, если пользователь ПОДТВЕРДИЛ
    if check_confirm('удаление выполнено'):
        task_list.pop(delete_edit - 1)
        show_message(message=delete_edit, mess_action="удалена")
    else:
        print("Удаление отменено.")
