def element_at(my_list, idx):
    for i in my_list:
        if idx < 0:
            return(None)
        elif idx >= len(my_lis):
            return(None)
        for i in range(len(my_list)):
            if i == idx:
                return(my_list[i])
        
