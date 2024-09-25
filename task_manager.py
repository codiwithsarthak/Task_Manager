#!/usr/bin/env python3
import curses
import os

# Define the filename where tasks will be stored
TASKS_FILE = 'tasks.txt'
tasks = []

# Function to load tasks from the specified file
def load_tasks():
    """Load tasks from the tasks.txt file."""
    if os.path.exists(TASKS_FILE):  # Check if the file exists
        with open(TASKS_FILE, 'r') as file:  # Open the file for reading
            # Read each line, strip whitespace, and return as a list
            return [line.strip() for line in file.readlines()]
    return []  # Return an empty list if the file does not exist

# Function to save the current tasks to the specified file
def save_tasks():
    """Save the current list of tasks to the tasks.txt file."""
    with open(TASKS_FILE, 'w') as file:  # Open the file for writing
        for task in tasks:  # Iterate through the tasks
            file.write(task + '\n')  # Write each task on a new line

def print_menu(stdscr, current_row):
    """Display the menu and highlight the current selection."""
    stdscr.clear()  # Clear the screen
    h, w = stdscr.getmaxyx()  # Get the height and width of the window

    # Define the menu options
    menu = ["Add Task", "View Tasks", "Delete Task", "Exit"]

    # Loop through each menu item and display it
    for idx, row in enumerate(menu):
        x = w // 2 - len(row) // 2  # Center the menu item
        y = h // 2 - len(menu) // 2 + idx  # Calculate the y position
        if idx == current_row:  # Highlight the current selection
            stdscr.attron(curses.color_pair(1))  # Turn on highlight
            stdscr.addstr(y, x, row)  # Display the highlighted item
            stdscr.attroff(curses.color_pair(1))  # Turn off highlight
        else:
            stdscr.addstr(y, x, row)  # Display the non-highlighted item

    stdscr.refresh()  # Refresh the screen to show the updates

def add_task(stdscr):
    """Prompt the user to add a new task."""
    curses.echo()  # Enable echoing of input
    stdscr.clear()  # Clear the screen
    stdscr.addstr(0, 0, "Enter a new task: ")  # Prompt for input
    task = stdscr.getstr(1, 0, 60).decode("utf-8")  # Get the task input
    tasks.append(task)  # Add the task to the list
    save_tasks()  # Save the updated task list to the file
    stdscr.addstr(3, 0, f"Task '{task}' added!")  # Confirm the addition
    stdscr.refresh()  # Refresh the screen
    stdscr.getch()  # Wait for user input

def view_tasks(stdscr):
    """Display the list of current tasks."""
    stdscr.clear()  # Clear the screen
    if not tasks:  # Check if there are no tasks
        stdscr.addstr(0, 0, "No tasks available.")  # Inform the user
    else:
        stdscr.addstr(0, 0, "Your tasks:")  # Header for the task list
        # Loop through tasks and display them
        for idx, task in enumerate(tasks):
            stdscr.addstr(idx + 1, 0, f"{idx + 1}. {task}")  # Display each task
    stdscr.refresh()  # Refresh the screen to show the updates
    stdscr.getch()  # Wait for user input

def delete_task(stdscr):
    """Prompt the user to delete a task by its number."""
    curses.echo()  # Enable echoing of input
    stdscr.clear()  # Clear the screen
    stdscr.addstr(0, 0, "Enter the task number to delete: ")  # Prompt for input
    task_number = stdscr.getstr(1, 0, 60).decode("utf-8")  # Get the task number

    try:
        task_idx = int(task_number) - 1  # Convert input to index
        if 0 <= task_idx < len(tasks):  # Check if the index is valid
            deleted_task = tasks.pop(task_idx)  # Remove the task
            save_tasks()  # Save the updated task list to the file
            stdscr.addstr(3, 0, f"Task '{deleted_task}' deleted!")  # Confirm deletion
        else:
            stdscr.addstr(3, 0, "Invalid task number.")  # Inform the user of invalid input
    except ValueError:
        stdscr.addstr(3, 0, "Please enter a valid number.")  # Handle invalid input

    stdscr.refresh()  # Refresh the screen
    stdscr.getch()  # Wait for user input

def main(stdscr):
    """Main function to run the task manager."""
    global tasks
    tasks = load_tasks()  # Load tasks at the start of the program
    curses.curs_set(0)  # Hide the cursor
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Initialize color pair

    current_row = 0  # Start with the first menu item selected

    while True:  # Main loop to display the menu and handle input
        print_menu(stdscr, current_row)  # Print the menu

        key = stdscr.getch()  # Get user input

        # Handle navigation and selection
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1  # Move selection up
        elif key == curses.KEY_DOWN and current_row < 3:
            current_row += 1  # Move selection down
        elif key == curses.KEY_ENTER or key in [10, 13]:  # Check for Enter key
            if current_row == 0:
                add_task(stdscr)  # Add a new task
            elif current_row == 1:
                view_tasks(stdscr)  # View current tasks
            elif current_row == 2:
                delete_task(stdscr)  # Delete a task
            elif current_row == 3:
                break  # Exit the program

        stdscr.refresh()  # Refresh the screen

# Start the curses application
curses.wrapper(main)
