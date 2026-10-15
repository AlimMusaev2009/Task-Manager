'''

    =====================================================

        Модуль показа информации в консоль

    =====================================================

'''


"""выводит список в консоль"""


def show_collection(task_list):
    print("=" * 30)
    tasks_for_view = []
    for number, task in enumerate(task_list):
        parts = task.split(" | ")  # Лучше разделять с пробелами
        if len(parts) >= 1:
            print(number + 1, parts[0])
            tasks_for_view.append(parts[1] if len(parts) > 1 else "Нет описания")

    selected_task = input("Выберите номер задачи для отображения описания или просто нажмите ENTER: ")
    if selected_task.isdigit():
        idx = int(selected_task) - 1
        if 0 <= idx < len(tasks_for_view):
            print("~" * 30)
            print(tasks_for_view[idx])
            print("~" * 30)
    print("=" * 30)

"""показывает список и ждёт завершение"""


def show_message(message=None, mess_action=None):
    if message is not None:
        print(f"задача {message} успешно {mess_action}")
    input("нажмите любую кнопу для продолжени")
