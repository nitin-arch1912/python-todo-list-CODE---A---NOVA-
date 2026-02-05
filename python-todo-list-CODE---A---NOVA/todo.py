import json
import os

FILENAME = "tasks.json"

# Load tasks from file


def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file


def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Add new task


def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print("✅ Task added successfully!")

# View tasks


def view_tasks(tasks):
    if not tasks:
        print("📭 No tasks available.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks):
        status = "✔" if task["completed"] else "✘"
        print(f"{i+1}. [{status}] {task['title']}")

# Mark task as completed


def complete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark complete: ")) - 1
        tasks[num]["completed"] = True
        save_tasks(tasks)
        print("🎉 Task marked as completed!")
    except:
        print("❌ Invalid input!")

# Delete task


def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(num)
        save_tasks(tasks)
        print(f"🗑 Task '{removed['title']}' deleted!")
    except:
        print("❌ Invalid input!")

# Main menu


def main():
    tasks = load_tasks()
    while True:
        print("\n====== TO-DO LIST MENU ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Exiting... Have a productive day!")
            break
        else:
            print("❌ Invalid choice!")


if __name__ == "__main__":
    main()
