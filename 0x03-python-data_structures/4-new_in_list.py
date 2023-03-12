#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx > 0:
        return(my_list.copy())
    if idx > len(my_list):
        return(my_list.copy())
    my_list.new_in_list()
    for i in my_list:
        if idx == i:
            print("{}". format(i))
