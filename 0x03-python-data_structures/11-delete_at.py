#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    newlist = my_list[:]
    listlen = len(my_list)
    if idx < 0 and idx >= listlen:
        return my_list
    else:
        del mylist[idx]
        return my_list
