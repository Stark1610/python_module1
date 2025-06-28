import os

FILE_NAME = "tasks.txt"
PRIORITETS = {"1": "низкий", "2": "средний", "3": "высокий"}
STATUS = {"1": "новая", "2": "в процессе", "3": "завершена"}


def load_file() -> dict:
    result = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            content = f.readlines()
            try :
                for str1 in content:
                    con = str1.strip("\n").split("/")
                    result[con[0]] = {
                        "title": con[1],
                        "description": con[2],
                        "priority": con[3],
                        "status": con[4],
                    }
            except:
                    return {}
    return result

def save_file(tasks : dict) -> None:

    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for key, task in tasks.items():
            f.write(
                f"{key}/{task["title"]}/{task["description"]}/{task["priority"]}/{task["status"]}\n"
            )

def get_next_id(tasks: dict) -> int:
    if tasks:
        max_id = max(int(task_id) for task_id in tasks.keys())
        return max_id + 1
    return 1


def new_task(tasks: dict, title: str, description: str, priority: str, status: str) -> None:
    task_id = str(get_next_id(tasks))
    tasks[task_id] = {
        "title": title,
        "description": description,
        "priority": PRIORITETS[priority],
        "status": STATUS[status],
    }
    save_file(tasks)


def print_tasks(tasks: dict) -> None:
    if tasks:
        for task_id, task in tasks.items():
            print("-" * 30)
            print(f"ID: {task_id}")
            print(f"  Название  : {task['title']}")
            print(f"  Описание  : {task['description']}")
            print(f"  Приоритет : {task['priority']}")
            print(f"  Статус    : {task['status']}")
            print("-" * 30)
    else:
        print("На данный момент задач нет")


def check_priority() -> str:
    while True:
        print("Выберите приоритет: 1 - низкий, 2 - средний, 3 - высокий")
        priority = input("Приоритет: ").strip()
        if priority in PRIORITETS:
            return priority
        print("Неверный ввод приоритета. Попробуйте снова.")


def check_status() -> str:
    while True:
        print("Выберите статус: 1 - новая, 2 - в процессе, 3 - завершена")
        status = input("Статус: ").strip()
        if status in STATUS:
            return status
        print("Неверный ввод статуса. Попробуйте снова.")

def search_task() -> None:
    tasks = load_file()
    word = input("Введите слово для поиска: ").strip().lower()
    found = {}

    for task_id, task in tasks.items():
        if word in task["title"].lower() or word in task["description"].lower():
            found[task_id] = task

    if found:
        print("\nНайденные задачи:")
        print_tasks(found)
    else:
        print("Задачи, содержащие указанное слово, не найдены.")


def delete_task(tasks: dict) -> None:
    task_id = input("Введите ID задачи для удаления: ").strip()
    if task_id in tasks:
        confirm = input(f"Вы уверены, что хотите удалить задачу '{tasks[task_id]['title']}'? (y/n): ").lower()
        if confirm == 'y':
            del tasks[task_id]
            save_file(tasks)
            print("Задача удалена.")
        else:
            print("Удаление отменено.")
    else:
        print("Задача с таким ID не найдена.") 


def edit_task(tasks: dict) -> None:
    task_id = input("Введите ID задачи, которую хотите отредактировать: ").strip()
    if task_id in tasks:
        task = tasks[task_id]
        print(f"Редактирование задачи ID {task_id}")

        title = input(f"Новое название ({task['title']}): ").strip() or task['title']
        description = input(f"Новое описание ({task['description']}): ").strip() or task['description']
        # priority = check_priority()
        # status = check_status()
        task["titlecheck_status()"] = title
        task["description"] = description
        task["priority"] = PRIORITETS[check_priority()]
        task["status"] = STATUS[check_status()]
        save_file(tasks)
        print("Задача успешно отредактирована!")
    else:
        print("Задача с таким ID не найдена.")


def main() -> None:
    tasks = load_file()

    while True:
        print("\nВыберите действие:")
        print("1 - Создать новую задачу")
        print("2 - Посмотреть список задач")
        print("3 - Найти задачи")
        print("4 - Удалить задачу")
        print("5 - Редактировать задачу")
        print("0 - Выйти из программы")

        choice = input("Введите номер действия: ").strip()

        if choice == "1":
            title = input("Введите название задачи: ").strip()
            description = input("Введите описание задачи: ").strip()
            priority = check_priority()
            status = check_status()
            new_task(tasks, title, description, priority, status)
            print("Новая задача успешно добавлена!")
        elif choice == "2":
            print_tasks(tasks)
        elif choice =="3":
            search_task()
        elif choice =="4":
            delete_task(tasks)
        elif choice =="5":
            edit_task(tasks)    
        elif choice == "0":
            print("Выход из программы")
            break
        else:
            print("Неверный ввод. Пожалуйста, введите 0, 1 или 2.")


if __name__ == "__main__":
    main()
