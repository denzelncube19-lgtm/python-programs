# Simple To-Do List
tasks = []
print("To-Do List App")
while True:
    print("\n1. Add Task  2. View Tasks  3. Mark Done  4. Exit")
    choice = input("Choose: ")
    if choice == '1':
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})
        print("Task added!")
    elif choice == '2':
        if not tasks:
            print("No tasks yet.")
        for i, t in enumerate(tasks, 1):
            status = "✓" if t["done"] else "○"
            print(f"  {i}. [{status}] {t['task']}")
    elif choice == '3':
        num = int(input("Enter task number to mark done: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = True
            print("Marked as done!")
    elif choice == '4':
        break
