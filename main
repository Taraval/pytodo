#!/usr/bin/python
import sys
import os
from sys import argv

TODO = "todo.txt"


def helpmenu():
    print "Please see documentation for more help."

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    print lines[line_num]
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()


def taskupdate():
    LINENUMBER = argv[2]
    LINEUPDATE = ' '.join(argv[3:])
    print "Updating task" + LINENUMBER + ": " + LINEUPDATE
    replace_line(TODO, int(LINENUMBER) - 1, LINEUPDATE + '\n')


def taskdelete():
    LINENUMBER = argv[2]
    print "Deleting task item " + LINENUMBER
    replace_line(TODO, int(LINENUMBER) - 1, '')


def taskcomplete():
    print "complete, or check"


def tasklist():
    with open(TODO, "r") as todoList:
        content = todoList.readlines()
        idx = 0
        for idx, x in enumerate(content):
            print str(idx + 1) + " " + x.strip()
        print "--"
        print "TODO: " + str(idx + 1) + " task total"


def taskadd():
    if os.path.exists(TODO):
        with open(TODO, "a+") as todoList:
            todo = ' '.join(sys.argv[2:])
            print "adding: " + todo
            todoList.write('\n' + todo)
    else:
        with open(TODO, "a+") as todoList:
            todo = ' '.join(sys.argv[2:])
            print "adding: " + todo
            todoList.write(todo)

""" Mapping the action key words """
cmd_map = {"add": taskadd, "ad": taskadd, "a": taskadd,
           "list": tasklist, "ls": tasklist, "l": tasklist,
           "delete": taskdelete, "del": taskdelete, "d": taskdelete,
           "update": taskupdate,
           "complete": taskcomplete
           }


def main():
    """ Main Function """
    get_cmd = argv[1]
    cmd_map.get(get_cmd, helpmenu)()

if __name__ == "__main__":
    #print ("Calling Main")
    main()
