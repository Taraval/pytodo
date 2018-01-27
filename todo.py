#!/usr/bin/python
import sys
import os
import re
from sys import argv

if os.environ.get('PYTODO'):
    __location__ = os.environ.get('PYTODO')
else:
    __location__ = os.environ.get('HOME') + "/.pytodo"

WS_FILE = __location__ + "/workspace"
WS_DEFAULT = "work"

if not os.path.exists(__location__):
    os.makedirs(__location__)

if os.path.isfile(WS_FILE):
    with open(WS_FILE) as f:
        WS_DEFAULT = f.read()
    f.closed
else:
    default_dir = open(WS_FILE,"w")
    default_dir.write(WS_DEFAULT)
    default_dir.close()

WS_STORE = __location__ + "/" + WS_DEFAULT

if not os.path.exists(WS_STORE):
    os.makedirs(WS_STORE)

TODO = WS_STORE + "/todo.txt"
DONE = WS_STORE + "/done.txt"


def help_menu():
    print("""t <action> <#> <value>

    add, ad, a           - add a task
    list, ls, l          - list all the task
    update, u            - update a task number
    priority, pri, p     - set the priority of the task
    done/complete, do    - mark task completed
    workspace, ws, w     - list/create/change workspace 
    workspacedelete, wd  - delete workspace
    """)


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
    try:
        item = argv[2]
    except:
        item = None
    if item != None:
        content = mod_task_read(TODO)
        new_content = content[int(item) - 1]
        del content[int(item) - 1]
        mod_task_write(TODO, content)
        content_done = mod_task_read(DONE)
        content_done.append(new_content)
        print("--")
        print("Todo task item " + item + " marked completed.")
        mod_task_write(DONE, content_done)
    else:
        content = mod_task_read(DONE)
        for idx, x in enumerate(content):
            print(str(idx + 1) + " " + x.strip())
        print("--")
        print("DONE: " + str(len(content)) + " task completed")


def task_list():
    try:
        item = argv[2]
    except:
        item = None

    if item != None:
        content = mod_task_read(TODO)
        new_content = content[int(item) - 1]
        print(item + " " + new_content.strip())
        print("--")
        print("TODO: " + str(len(content)) + " task total")
    else:
        content = mod_task_read(TODO)
        for idx, x in enumerate(content):
            print(str(idx + 1) + " " + x.strip())
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


def task_workspace():
    try:
        item = argv[2]
    except:
        item = None

    if item != None:
        WS_STORE = __location__ + "/" + item
        if not os.path.exists(WS_STORE):
            print("No %s workspace, do you want to create? Please enter (y/n) " %item)
            ws_new = False
            yes = {'yes','y', 'ye', ''}
            choice = raw_input().lower()
            if choice in yes:
                ws_new = True
            if ws_new:
                os.makedirs(WS_STORE)
                default_dir = open(WS_FILE,"w")
                default_dir.write(item)
                default_dir.close()
                print("--")
                print("WORKSPACE: [%s]" %tem)
        else:
            default_dir = open(WS_FILE,"w")
            default_dir.write(item)
            default_dir.close()
            print("--")
            print("WORKSPACE: [%s]" %item)
    else:
        with open(WS_FILE) as f:
            WS_DEFAULT = f.read()
        f.closed
        print("ACTIVE WORKSPACE: [%s]" %WS_DEFAULT)
        print("--")
        ws_list = ""
        for root, dirs, files in os.walk(__location__):
            if dirs:
                ws_list += ', '.join(dirs)
        print("AVAILABLE WORKSPACES: [%s]" %ws_list)

def task_workspacedelete():
    try:
        item = argv[2]
    except:
        item = None

    if item != None:
        WS_STORE = __location__ + "/" + item
        if os.path.exists(WS_STORE):
            print("Do you want to delete [%s] workspace? Please enter (y/n) " %item)
            ws_delete = False
            yes = {'yes','y', 'ye', ''}
            choice = raw_input().lower()
            if choice in yes:
                ws_delete= True
            if ws_delete:
                os.rmdir(WS_STORE)
    else:
        print("Please recareful on deleting workspace")
 

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
           "delete": task_delete, "del": task_delete, "de": task_delete,
           "update": task_update, "up": task_update, "u": task_update,
           "priority": task_priority, "pri": task_priority, "p": task_priority,
           "complete": task_complete, "com": task_complete, "c": task_complete, "done": task_complete, "d": task_complete,
           "workspace": task_workspace, "ws": task_workspace, "w": task_workspace,
           "workspacedelete": task_workspacedelete, "wsdelete": task_workspacedelete, "wd": task_workspacedelete
           }


def main():
    """ Main Function """
    try:
        get_cmd = argv[1]
    except:
        get_cmd = "list"
    cmd_map.get(get_cmd, help_menu)()

if __name__ == "__main__":
    main()
