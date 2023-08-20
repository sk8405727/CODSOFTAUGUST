class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added:", task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed:", task)
        else:
            print("Task not found")

    def show_tasks(self):
        if self.tasks:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks in the list")

    def update_task(self, old_task, new_task):
        if old_task in self.tasks:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task
            print("Task updated:", old_task, "->", new_task)
        else:
            print("Task not found")

    def clear_tasks(self):
        self.tasks = []
        print("All tasks cleared")


def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4. Update task")
        print("5. Clear all tasks")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.show_tasks()
        elif choice == "4":
            old_task = input("Enter task to update: ")
            new_task = input("Enter new task: ")
            todo_list.update_task(old_task, new_task)
        elif choice == "5":
            todo_list.clear_tasks()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
