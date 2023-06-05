from my_functions.classes import *


def read_file(file_name):
    file_input = open(file_name, "r")

    # skip the header
    file_input.readline()

    list_items = []
    for line in file_input:
        elements = line.strip().split(';')
        new_item = Item(elements[0], elements[1], elements[2], elements[3], elements[4], elements[5], elements[6],
                        elements[7], elements[8], elements[9])
        list_items.append(new_item)

    file_input.close()

    my_wardrobe = Wardrobe(list_items)
    print(my_wardrobe)
    return my_wardrobe
