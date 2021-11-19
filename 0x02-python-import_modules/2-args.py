#!/usr/bin/python3
if __name__ == "__main__":
    import sys as ag
    argc = len(ag.argv)
    args = ag.argv
    arg = argc - 1
    if arg == 0:
        print("{} arguments.".format(arg))
    elif arg == 1:
        print("{} argument:".format(arg))
        print("1: {}".format(args[1]))
    else:
        print("{} arguments:".format(arg))
        i = 1
        while i >= 1 and i < argc:
            print("{}: {}".format(i, args[i]))
            i += 1
