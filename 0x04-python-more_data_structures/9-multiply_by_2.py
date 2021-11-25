#!/usr/bin/python3
def multiply_by_2(my_dict):
    mynew_dict = {}
    for key, val in my_dict.items():
        mynew_dict[key] = val * 2
    return mynew_dict
