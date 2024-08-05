import json

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"{self.description} - {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task number.")

def save_tasks_to_file(todo_list, filename):
    with open(filename, 'w') as file:
        tasks = [{'description': task.description, 'completed': task.completed} for task in todo_list.tasks]
        json.dump(tasks, file)

def load_tasks_from_file(filename):
    todo_list = ToDoList()
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
            for task_data in tasks:
                task = Task(task_data['description'])
                task.completed = task_data['completed']
                todo_list.tasks.append(task)
    except FileNotFoundError:
        pass
    return todo_list

def main():
    todo_list = load_tasks_from_file('tasks.json')

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.mark_task_completed(index)
        elif choice == '4':
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '5':
            save_tasks_to_file(todo_list, 'tasks.json')
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
