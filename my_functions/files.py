import csv
from dataclasses import dataclass

from my_functions.classes import *


@dataclass
class Item1:
    name: str
    price: float = 0.0
    description: str = ''


def read_file(file_name):
    # file_input = open(file_name, "r")
    #
    # # skip the header
    # header = file_input.readline().strip().split(";")
    #
    # list_items = []
    # new_dict = {}
    # for line in file_input:
    #     elements = line.strip().split(';')
    #     # new_item = Item(elements[0], elements[1], elements[2], elements[3], elements[4], elements[5], elements[6],
    #     #                 elements[7], elements[8], elements[9])
    #     index = 0
    #     for element in elements:
    #         new_dict.update({header[index]: element})
    #         index += 1
    #     new_item = Item(**new_dict)
    #     list_items.append(new_item)
    #
    # file_input.close()
    #
    # my_wardrobe = Wardrobe(list_items)
    # print(my_wardrobe)
    # return my_wardrobe

    with open(file_name, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        list_items = [Item(**row) for row in reader]

        my_wardrobe = Wardrobe(list_items)
        print(my_wardrobe)
        return my_wardrobe


def write_file(file_name, my_wardrobe):
    # file_result = open(file_name, "w")
    # file_result.write("name;item_class;item_type;size;season;color;brand;storage;price;description\n")
    # for element in my_wardrobe.list_items():
    #     file_result.write(element.fullstr(";") + "\n")
    #
    # file_result.close()
    # print(f'file {file_name} is updated')

    # this code doesn't work because attribute name in object Item is privet
    # and Item.__dict__.keys() return name "_Item__name" when required "name"

    with open(file_name, 'w') as csvfile:
        list_items = my_wardrobe.list_items()
        writer = csv.DictWriter(csvfile, fieldnames=list_items[0].__dict__.keys(), delimiter=';', lineterminator='\n')
        writer.writeheader()
        writer.writerows([item.__dict__ for item in list_items])
