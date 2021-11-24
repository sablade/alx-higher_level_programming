#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    newlist = my_list[:]
    listlen = len(my_list) - 1
    if listlen < 0 or listlen < idx:
        return my_list
    else:
        del mylist[idx]
        return my_list
