#!/usr/bin/python3
def replace_in_list(my_list, idx, element):

    if idx < 0:
        return(my_list)
    elif idx > my_list:
        return(my_list)
    for i in range(my_list):
        if idx == i:
            print("my_lis[i]".format(i))
