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


def write_file(file_name, my_wardrobe):
    file_result = open(file_name, "w")
    file_result.write("name;item_class;item_type;size;season;color;brand;storage;price;description\n")
    for element in my_wardrobe.list_items():
        file_result.write(element.fullstr() + "\n")

    file_result.close()
    print(f'file {file_name} is updated')
