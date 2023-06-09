import csv
from my_functions.classes import *


def read_file(file_name):
    with open(file_name, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        list_items = [Item(**row) for row in reader]

        my_wardrobe = Wardrobe(list_items)
        print(my_wardrobe)
        return my_wardrobe


def write_file(file_name, my_wardrobe):
    with open(file_name, 'w') as csvfile:
        list_items = my_wardrobe.list_items()
        writer = csv.DictWriter(csvfile, fieldnames=list_items[0].__dict__.keys(), delimiter=';', lineterminator='\n')
        writer.writeheader()
        writer.writerows([item.__dict__ for item in list_items])
        print(f'file {file_name} is updated')
