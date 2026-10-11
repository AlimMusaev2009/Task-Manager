'''

    =====================================================

        Модуль показа информации в консоль

    =====================================================

'''


"""выводит список в консоль"""


def show_collection(task_list):
    print("=" * 30)
    full_task_list = []
    for number, task in enumerate(task_list):
        full_task_list = task.split("|")
        print(number + 1, full_task_list[0])
        full_task_list.append(full_task_list[0])
    selected_task = input("Выбирите номер задачи для отображения описания или просто нажмите ENTER")
    if selected_task.isdigit():
        print("~" * 30)
        print(full_task_list[int(selected_task) - 1])
        print("~" * 30)
    print("=" * 30)

"""показывает список и ждёт завершение"""


def show_message(message=None, mess_action=None):
    if message is not None:
        print(f"задача {message} успешно {mess_action}")
    input("нажмите любую кнопу для продолжени")
