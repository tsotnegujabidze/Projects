def task_manager():
    tasks = []

    while True:
        print("\nTask Manager:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Select an option (1/2/3/4/5): ")

        if choice == '1':
            task_description = input("Enter the task description: ")
            tasks.append({"description": task_description, "completed": False})
        elif choice == '2':
            for index, task in enumerate(tasks, start=1):
                status = "Done" if task["completed"] else "Pending"
                print(f"{index}. {task['description']} - {status}")
        elif choice == '3':
            task_index = int(input("Enter the task number to complete: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["completed"] = True
                print("Task marked as completed.")
        elif choice == '4':
            task_index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks.pop(task_index)
                print("Task deleted.")
        elif choice == '5':
            print("Hope you managed to finish all of your tasks! Goodbye!")
            break


task_manager()