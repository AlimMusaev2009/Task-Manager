"""загрузка"""

def load_collection(task_list, file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                # Пропускаем пустые строки
                if line.strip():
                    task_list.append(line.strip())
    except FileNotFoundError:
        # Если файла нет, просто возвращаем пустой список
        pass
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
    return task_list

"""сохранение"""

def save_collection(task_list, file_name):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            for task in task_list:
                file.write(f"{task}\n")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")
