'''
    =====================================================
        Модуль показа информации в консоль
    =====================================================
'''

def show_collection(task_list):
    """Выводит список задач в консоль."""
    print("=" * 30)
    if not task_list:
        print("Список задач пуст.")
        print("=" * 30)
        return

    # Выводим список
    for number, task in enumerate(task_list):
        # Предполагаем, что формат "Имя|Описание"
        parts = task.split("|")
        name = parts[0]
        print(f"{number + 1}. {name}")
    
    print("=" * 30)
    
    selected_task = input("Выберите номер задачи для отображения описания или просто нажмите ENTER: ").strip()
    
    if selected_task.isdigit():
        idx = int(selected_task) - 1
        if 0 <= idx < len(task_list):
            parts = task_list[idx].split("|")
            description = parts[1] if len(parts) > 1 else "Описание отсутствует"
            print("~" * 30)
            print(f"Задача: {parts[0]}")
            print(f"Описание: {description}")
            print("~" * 30)
        else:
            print("Неверный номер задачи.")
    print("=" * 30)

def show_message(message=None, mess_action=None):
    """Показывает сообщение и ждет нажатия клавиши."""
    if message is not None:
        print(f"Задача {message} успешно {mess_action}")
    input("нажмите Enter для продолжения...")
