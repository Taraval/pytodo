#!/usr/bin/python
import sys
import os
import re
from sys import argv

TODO = "todo.txt"
DONE = "todo-done.txt"


def help_menu():
    print("Please see documentation for more help.")


def task_update():
    item = argv[2]
    lineupdate = ' '.join(argv[3:])
    print("Updating task" + item + ": " + lineupdate)
    content = mod_task_read(TODO)
    content[int(item) - 1] = lineupdate + "\n"
    mod_task_write(TODO, content)


def task_delete():
    item = argv[2]
    print("Deleting task item " + item)
    content = mod_task_read(TODO)
    del content[int(item) - 1]
    print("--")
    print("TODO: " + str(len(content)) + " task total")
    mod_task_write(TODO, content)


def task_complete():
    item = argv[2]
    content = mod_task_read(TODO)
    new_content = content[int(item) - 1]
    del content[int(item) - 1]
    mod_task_write(TODO, content)
    content_done = mod_task_read(DONE)
    content_done.append(new_content)
    print("--")
    print("Todo task item " + item + " marked completed.")
    mod_task_write(DONE, content_done)


def task_list():
    try:
        item = argv[2]
    except:
        item = None

    if item != None:
        content = mod_task_read(TODO)
        new_content = content[int(item) - 1]
        print item + " " + new_content.strip()
        print("--")
        print("TODO: " + str(len(content)) + " task total")
    else:
        content = mod_task_read(TODO)
        for idx, x in enumerate(content):
            print str(idx + 1) + " " + x.strip()
        print("--")
        print("TODO: " + str(len(content)) + " task total")


def task_add():
    content = mod_task_read(TODO)
    todo = ' '.join(sys.argv[2:])
    print("Adding: " + todo)
    content.append(todo + "\n")
    print("--")
    print("TODO: " + str(len(content)) + " task total")
    mod_task_write(TODO, content)


def task_priority():
    try:
        item = argv[2]
        mode = argv[3]
    except:
        item = None
    if item != None:
        content = mod_task_read(TODO)
        new_content = content[int(item) - 1]
        new_content = re.sub("^\(.*\)\ ", "", new_content)
        if mode != "-":
            print("Update task " + item + " with priority (" + mode.upper() + ") ")
            new_content = "(" + mode.upper() + ") " + new_content
        else:
            print("Remove priority task " + item)

        content[int(item) - 1] = new_content
        mod_task_write(TODO, content)
    else:
        print("Please RTFM")


def mod_task_read(_file_):
    if os.path.exists(_file_):
        with open(_file_, "r") as todoList:
            results = todoList.readlines()
        return results
    else:
        return []


def mod_task_write(_file_, content):
    with open(_file_, "w") as todoList:
        todoList.writelines(content)


""" Mapping the action key words """
cmd_map = {"add": task_add, "ad": task_add, "a": task_add,
           "list": task_list, "ls": task_list, "l": task_list,
           "delete": task_delete, "del": task_delete, "d": task_delete,
           "update": task_update, "up": task_update, "u": task_update,
           "priority": task_priority, "pri": task_priority, "p": task_priority,
           "complete": task_complete, "com": task_complete, "c": task_complete
           }


def main():
    """ Main Function """
    try:
        get_cmd = argv[1]
    except:
        get_cmd = "list"
    cmd_map.get(get_cmd, help_menu)()

if __name__ == "__main__":
    #print ("Calling Main")
    main()
