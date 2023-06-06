from my_functions.classes import *


def read_file(file_name):
    file_input = open(file_name, "r")

    # skip the header
    file_input.readline()

    list_items = []
    for line in file_input:
        elements = line.strip().split(';')
        new_item = Item(elements[0].strip(), elements[1].strip(), elements[2].strip(), elements[3].strip(),
                        elements[4].strip(), elements[5].strip(), elements[6].strip(), elements[7].strip(),
                        elements[8].strip(), elements[9].strip())
        list_items.append(new_item)

    file_input.close()

    my_wardrobe = Wardrobe(list_items)
    print(my_wardrobe)
    return my_wardrobe


def write_file(file_name, my_wardrobe):
    file_result = open(file_name, "w")
    file_result.write("name; item_class; item_type; size; season; color; brand; storage; price; description\n")
    for element in my_wardrobe.list_items():
        file_result.write(element.fullstr() + "\n")

    file_result.close()
    print(f'file {file_name} is updated')
