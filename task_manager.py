import curses
import os
import json

# Define the filename where tasks will be stored
TASKS_FILE = 'tasks.json'
tasks = []

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks():
    """Save the current list of tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def print_menu(stdscr, current_row, menu):
    """Display the main menu with highlights, title, and navigation instructions."""
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    # Display centered title
    title = "Task Manager"
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(1, w // 2 - len(title) // 2, title)
    stdscr.attroff(curses.color_pair(1))

    # Define and display the menu options
    menu = ["Add Task", "View Tasks", "Toggle Completion", "Edit Task", "Delete Task", "Exit"]
    for idx, row in enumerate(menu):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu) // 2 + idx
        if idx == current_row:
            stdscr.attron(curses.color_pair(1))  # Highlight selected item
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.attron(curses.color_pair(2))  # Regular menu color
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(2))

    # Add navigation instructions at the bottom
    instructions = "Use arrow keys to navigate and Enter to select."
    stdscr.attron(curses.color_pair(2))
    stdscr.addstr(h - 2, w // 2 - len(instructions) // 2, instructions)
    stdscr.attroff(curses.color_pair(2))

    stdscr.refresh()

def add_task(stdscr):
    """Prompt the user to add a new task."""
    curses.echo()
    stdscr.clear()
    stdscr.addstr(0, 0, "Enter a new task: ")
    task_description = stdscr.getstr(1, 0, 60).decode("utf-8")
    task = {"description": task_description, "completed": False}
    tasks.append(task)
    save_tasks()
    stdscr.addstr(3, 0, f"Task '{task_description}' added!")
    stdscr.refresh()
    stdscr.getch()

def toggle_task_completion(stdscr):
    """Toggle a task's completion status."""
    curses.echo()
    stdscr.clear()
    stdscr.addstr(0, 0, "Enter the task number to toggle completion: ")
    task_number = stdscr.getstr(1, 0, 60).decode("utf-8")

    try:
        task_idx = int(task_number) - 1
        if 0 <= task_idx < len(tasks):
            tasks[task_idx]["completed"] = not tasks[task_idx]["completed"]
            save_tasks()
            status = "completed" if tasks[task_idx]["completed"] else "pending"
            stdscr.addstr(3, 0, f"Task marked as {status}.")
        else:
            stdscr.addstr(3, 0, "Invalid task number.")
    except ValueError:
        stdscr.addstr(3, 0, "Please enter a valid number.")
    stdscr.refresh()
    stdscr.getch()

def view_tasks(stdscr):
    """Display the list of tasks with completion status."""
    stdscr.clear()
    if not tasks:
        stdscr.addstr(0, 0, "No tasks available.")
    else:
        stdscr.addstr(0, 0, "Your tasks:")
        for idx, task in enumerate(tasks):
            status = "✓" if task["completed"] else "✗"
            stdscr.addstr(idx + 1, 0, f"{idx + 1}. {task['description']} [{status}]")
    stdscr.refresh()
    stdscr.getch()

def delete_task(stdscr):
    """Delete a task by its number."""
    curses.echo()
    stdscr.clear()
    stdscr.addstr(0, 0, "Enter the task number to delete: ")
    task_number = stdscr.getstr(1, 0, 60).decode("utf-8")

    try:
        task_idx = int(task_number) - 1
        if 0 <= task_idx < len(tasks):
            deleted_task = tasks.pop(task_idx)
            save_tasks()
            stdscr.addstr(3, 0, f"Task '{deleted_task['description']}' deleted!")
        else:
            stdscr.addstr(3, 0, "Invalid task number.")
    except ValueError:
        stdscr.addstr(3, 0, "Please enter a valid number.")
    stdscr.refresh()
    stdscr.getch()

def edit_task(stdscr):
    """Edit the description of a task."""
    curses.echo()
    stdscr.clear()
    stdscr.addstr(0, 0, "Enter the task number to edit: ")
    task_number = stdscr.getstr(1, 0, 60).decode("utf-8")

    try:
        task_idx = int(task_number) - 1
        if 0 <= task_idx < len(tasks):
            stdscr.addstr(2, 0, "Enter the new description: ")
            new_description = stdscr.getstr(3, 0, 60).decode("utf-8")
            tasks[task_idx]["description"] = new_description
            save_tasks()
            stdscr.addstr(5, 0, "Task description updated!")
        else:
            stdscr.addstr(2, 0, "Invalid task number.")
    except ValueError:
        stdscr.addstr(2, 0, "Please enter a valid number.")
    stdscr.refresh()
    stdscr.getch()

def main(stdscr):
    global tasks
    tasks = load_tasks()
    curses.curs_set(0)  # Hide the cursor
    
    # Initialize color pairs for the interface
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Highlight color
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Regular menu color

    menu = ["Add Task", "View Tasks", "Toggle Completion", "Edit Task", "Delete Task", "Exit"]  # Define menu here
    current_row = 0
    while True:
        print_menu(stdscr, current_row, menu)  # Pass menu to print_menu
        key = stdscr.getch()

        # Handle navigation and selection
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == 0:
                add_task(stdscr)
            elif current_row == 1:
                view_tasks(stdscr)
            elif current_row == 2:
                toggle_task_completion(stdscr)
            elif current_row == 3:
                edit_task(stdscr)
            elif current_row == 4:
                delete_task(stdscr)
            elif current_row == 5:
                break

        stdscr.refresh()

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except Exception as e:
        print(f"An error occurred: {e}")
    # Remove the curses.endwin() line as it's automatically called by curses.wrapper()
