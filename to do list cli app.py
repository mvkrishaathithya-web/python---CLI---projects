tasks = []

while True:
    print("\nTo-Do List App")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")

    choice = input("Choose an option (1/2/3/4): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print(f"Task '{task}' has been added.")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour To-Do List:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    elif choice == "3":
        if len(tasks)== 0:
            print("no tasks found")
        else:
            num_task=int(input("enter the number of the task to delete: "))
            print(f"{tasks.pop(num_task-1)} has been deleted")

    elif choice == "4":
        print("Goodbye!")
        break
