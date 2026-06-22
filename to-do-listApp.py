import json
import os

DATA_FILE = "tools.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def show_menu():
    print("\n===== TO-DO LIST APP ======")
    print("1. View Tasks")
    print("2. Add Tasks")
    print("3. Mark Task as Done ")
    print("4. Delete Task")
    print("5. Exit")


def view_tasks(tasks):
    print("\n--- Your Task ---")
    if not tasks:
        print("No task yet. Add one!")
        return 
    for i, task in enumerate(tasks, start =1):
        status = "done" if task["done"] else "not"
        print(f"{i}.[{status}] {task['title']}")


def add_task(tasks):
    title = input("Enter new task: ").strip()
    if title:
        tasks.append({"title" : title, "done": False})
        save_tasks(tasks)
        print(f'Task "{title}" added!')
    
    else:
        print("Task cannot be empty .")



def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return 
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as done!")

        else:
            print("Invalid task number .")

    except ValueError:
        print("Please enter a valid number .")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return 
    try:
        num = int(input("Enter task number to delete : "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f'Task "{removed["title"]}" deleted!')
        

        else:
            print("Invalid task number .")

    except ValueError:
        print("Please enter a valid number. ")



def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()


        if choice == "1":
            view_tasks(tasks)
        elif choice =="2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice =="4":
            delete_task(tasks)
        elif choice == "5":
            break

        else:
            print("Invalid choice , try again. ")


if __name__ == "__main__":
    main()


        

