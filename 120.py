def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = [line.strip().split(' - ') for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f"{task[0]} - {task[1]}\n")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append([task, "Pending"])
    print("Task added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
    else:
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task[0]} - {task[1]}")

def mark_task_done(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1][1] = "Done"
            print(f"Task '{tasks[task_num - 1][0]}' marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task[0]}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def main():
    filename = 'tasks.txt'
    tasks = load_tasks(filename)

    while True:
        print("\nTo-Do List Manager")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as done")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(filename, tasks)
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
