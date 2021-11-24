#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listLen = len(my_list)
    newList = my_list
    if idx < 0:
        print(newList)
    elif idx >= listLen:
        print(newList)
    else:
        my_list[idx] = element
