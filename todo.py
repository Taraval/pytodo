#!/usr/bin/python
import sys
import os
from sys import argv

TODO = "todo.txt"


def help_menu():
    print("Please see documentation for more help.")


def task_update():
    linenumber = argv[2]
    lineupdate = ' '.join(argv[3:])
    print("Updating task" + linenumber + ": " + lineupdate)
    content = mod_task_read()
    content[int(linenumber) - 1] = lineupdate + '\n'
    mod_task_write(content)


def task_delete():
    linenumber = argv[2]
    print("Deleting task item " + linenumber)
    content = mod_task_read()
    content[int(linenumber) - 1] = ""
    print("--")
    print("TODO: " + str(len(content) - 1) + " task total")
    mod_task_write(content)


def task_complete():
    print("complete, or check")


def task_list():
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
           "update": task_update,
           "complete": task_complete
           }


def main():
    """ Main Function """
    get_cmd = argv[1]
    cmd_map.get(get_cmd, help_menu)()

if __name__ == "__main__":
    #print ("Calling Main")
    main()

