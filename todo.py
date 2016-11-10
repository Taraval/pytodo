#!/usr/bin/python
import sys
import os
import re
from sys import argv

TODO = "todo.txt"


def help_menu():
    print("Please see documentation for more help.")


def task_update():
    item = argv[2]
    lineupdate = ' '.join(argv[3:])
    print("Updating task" + item + ": " + lineupdate)
    content = mod_task_read()
    content[int(item) - 1] = lineupdate + "\n"
    mod_task_write(content)


def task_delete():
    item = argv[2]
    print("Deleting task item " + item)
    content = mod_task_read()
    del content[int(item) - 1]
    print("--")
    print("TODO: " + str(len(content)) + " task total")
    mod_task_write(content)


def task_complete():
    print("complete, or check")


def task_list():
    try:
        item = argv[2]
    except:
        item = None

    if item != None:
        content = mod_task_read()
        new_content = content[int(item) - 1]
        print item + " " + new_content.strip()
        print("--")
        print("TODO: " + str(len(content)) + " task total")
    else:
        content = mod_task_read()
        for idx, x in enumerate(content):
            print str(idx + 1) + " " + x.strip()
        print("--")
        print("TODO: " + str(len(content)) + " task total")


def task_add():
    content = mod_task_read()
    todo = ' '.join(sys.argv[2:])
    print("Adding: " + todo)
    content.append(todo + "\n")
    print("--")
    print("TODO: " + str(len(content)) + " task total")
    mod_task_write(content)


def task_priority():
    try:
        item = argv[2]
        mode = argv[3]
    except:
        item = None
    if item != None:
        content = mod_task_read()
        new_content = content[int(item) - 1]
        new_content = re.sub("^\(.*\)\ ", "", new_content)
        if mode != "-":
            print("Update task " + item + " with priority (" + mode.upper() + ") ")
            new_content = "(" + mode.upper() + ") " + new_content
        else:
            print("Remove priority task " + item)

        content[int(item) - 1] = new_content
        mod_task_write(content)
    else:
        print("Please RTFM")

def mod_task_read():
    if os.path.exists(TODO):
        with open(TODO, "r") as todoList:
            results = todoList.readlines()
        return results
    else:
        return []


def mod_task_write(content):
    with open(TODO, "w") as todoList:
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
    get_cmd = argv[1]
    cmd_map.get(get_cmd, help_menu)()

if __name__ == "__main__":
    #print ("Calling Main")
    main()
