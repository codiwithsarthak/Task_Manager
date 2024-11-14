# Task Manager CLI

A terminal-based Task Manager built with Python and `curses`. This application provides a straightforward way to manage your tasks from the command line, offering features such as task addition, editing, completion toggling, and deletion. 

## Features
- **Add Task**: Add new tasks to your list easily.
- **View Tasks**: View all tasks along with their current completion status.
- **Toggle Completion**: Mark tasks as complete or incomplete.
- **Edit Task**: Modify existing task descriptions.
- **Delete Task**: Remove tasks that are no longer needed.
- **User-friendly CLI Navigation**: Simple keyboard navigation with clear instructions.

## Requirements
- **Python 3**: Required to run the script. You can check your version with:
  ```bash
  python3 --version
  ```
- **`curses` Library**: This library is typically pre-installed on Linux and macOS. Windows users may need to install a compatible version (e.g., `windows-curses`).

## Installation

1. **Clone the Repository**:
   Download the repository to your local machine:
   ```bash
   git clone https://github.com/codiwithsarthak/Task_Manager.git
   cd Task_Manager
   ```

2. **Make the Script Executable**:
   Give execute permissions to the main script:
   ```bash
   chmod +x task_manager.py
   ```

3. **Run the Application**:
   Start the Task Manager using Python 3:
   ```bash
   python3 task_manager.py
   ```

## Usage

Once running, the Task Manager CLI application provides a menu-based interface for task management. 

- **Navigation**:
  - **Up/Down Arrow Keys**: Move through the menu options.
  - **Enter**: Select the highlighted option.
- **Menu Options**:
  - **Add Task**: Enter a new task description, and it will be saved to the list.
  - **View Tasks**: See a list of all tasks, with symbols to indicate their completion status.
  - **Toggle Completion**: Mark tasks as complete or incomplete by entering the task number.
  - **Edit Task**: Update the description of a specific task.
  - **Delete Task**: Permanently remove a task from the list.
  - **Exit**: Close the application.

Your tasks are saved in a `tasks.json` file within the project directory, so they persist between sessions.

## Creating a Desktop Shortcut (.desktop file)

To launch the Task Manager CLI from your desktop environment’s application menu, you can create a `.desktop` file. This setup allows for convenient access on Linux-based systems.

### Steps:

1. **Create the `.desktop` File**:
   Open a text editor and create a new file named `task_manager.desktop` with the following content:

   ```ini
   [Desktop Entry]
   Version=1.0
   Name=Task Manager CLI
   Comment=A terminal-based task manager application
   Exec=python3 /path/to/task_manager_cli/task_manager.py
   Icon=utilities-terminal
   Terminal=true
   Type=Application
   Categories=Utility;
   ```

   - **`Exec`**: Replace `/path/to/task_manager_cli/task_manager.py` with the full path to your `task_manager.py` file.
   - **`Icon`**: You can change this to a custom icon path if desired.

2. **Move the `.desktop` File to the Applications Directory**:
   Copy the `.desktop` file to the appropriate directory to make it available in your application menu:

   ```bash
   sudo cp task_manager.desktop /usr/share/applications/
   ```

3. **Update Application Menus**:
   Depending on your desktop environment, you may need to refresh the application menu or log out and log back in to see the new entry.

4. **Launch from Menu**:
   Search for "Task Manager CLI" in your applications menu, and it should appear with the terminal icon. Selecting it will open your task manager in a terminal window.

## Directory Structure

The project directory contains the following:

```
task_manager_cli/
│
├── task_manager.py       # Main script for Task Manager CLI
├── tasks.json            # Data file to store tasks (auto-generated after first run)
└── task_manager.desktop  # Optional .desktop file for easy application menu access
```

## Troubleshooting

### Common Issues
- **Error `_curses.error: endwin() returned ERR`**: This error typically occurs if the terminal does not support `curses`. Make sure to run the script in a compatible terminal emulator.
- **Task File Not Found**: If `tasks.json` is missing, it will be created automatically on the first run. Ensure you have write permissions in the script's directory.

### Customizing the .desktop File
You can customize the `.desktop` file with your preferred terminal emulator or icon, if desired.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
