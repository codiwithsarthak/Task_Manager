#!/usr/bin/env python3
import curses
import os

tasks = []

def print_menu(stdscr, current_row):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    menu = ["Add Task", "View Tasks", "Delete Task", "Exit"]

    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == current_row:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()

def add_task(stdscr):
    curses.echo()
    stdscr.clear()
    stdscr.addstr(0, 0, "Enter a new task: ")
    task = stdscr.getstr(1, 0, 60).decode("utf-8")
    tasks.append(task)
    stdscr.addstr(3, 0, f"Task '{task}' added!")
    stdscr.refresh()
    stdscr.getch()

def view_tasks(stdscr):
    stdscr.clear()
    if not tasks:
        stdscr.addstr(0, 0, "No tasks available.")
    else:
        stdscr.addstr(0, 0, "Your tasks:")
        for idx, task in enumerate(tasks):
            stdscr.addstr(idx + 1, 0, f"{idx + 1}. {task}")
    stdscr.refresh()
    stdscr.getch()

def delete_task(stdscr):
    curses.echo()
    stdscr.clear()
    stdscr.addstr(0, 0, "Enter the task number to delete: ")
    task_number = stdscr.getstr(1, 0, 60).decode("utf-8")

    try:
        task_idx = int(task_number) - 1
        if 0 <= task_idx < len(tasks):
            deleted_task = tasks.pop(task_idx)
            stdscr.addstr(3, 0, f"Task '{deleted_task}' deleted!")
        else:
            stdscr.addstr(3, 0, "Invalid task number.")
    except ValueError:
        stdscr.addstr(3, 0, "Please enter a valid number.")

    stdscr.refresh()
    stdscr.getch()

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_row = 0

    while True:
        print_menu(stdscr, current_row)

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < 3:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == 0:
                add_task(stdscr)
            elif current_row == 1:
                view_tasks(stdscr)
            elif current_row == 2:
                delete_task(stdscr)
            elif current_row == 3:
                break

        stdscr.refresh()

curses.wrapper(main)

