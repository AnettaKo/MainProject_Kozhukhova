import plotly.figure_factory as ff
from my_functions.classificators import *


def table_report(my_wardrobe, select=False):
    list_items = my_wardrobe.list_items()
    if len(list_items) == 0:
        print('no items in wardrobe')
        return

    if select:
        selections = {}

        list_attributes = ['item_class', 'item_type', 'size', 'season', 'color', 'brand']
        list_attributes_selected = []

        add_attribute = True
        while add_attribute:
            attribute = input_from_classificator(list_attributes, 'attribute for selection')
            list_attributes_selected.append(attribute)
            list_attributes.remove(attribute)

            list_values = []
            for element in list_items:
                list_values.append(element.__getattribute__(attribute))
            list_values = list(set(list_values))
            list_values = sorted(list_values)

            list_values_selected = []

            add_value = True
            while add_value:
                value = input_from_classificator(list_values, f'values "{attribute}" for selection')
                list_values_selected.append(value)
                list_values.remove(value)

                answer = input(f'Do you wont to add new value of "{attribute}" to selection? '
                               f'Yes - 1, No - any other key: ')
                if answer != "1":
                    add_value = False

            selections.update({attribute: list_values_selected})

            answer = input("Do you wont to add new attribute to selection? Yes - 1, No - any other key: ")
            if answer != "1":
                add_attribute = False

        print(selections)
        list_items_selected = list_items

        for attribute, selection in selections.items():

            list_items_selected = filter(lambda item: item.__getattribute__(attribute) in selection,
                                         list_items_selected)
            list_items_selected = (list(list_items_selected))

        print([str(element) for element in list_items_selected])

        if len(list_items_selected) == 0:
            print('no items in result table')
            return

    else:
        list_items_selected = list_items

    cells = [list(item.__dict__.values()) for item in list_items_selected]
    cells.insert(0, list(list_items[0].__dict__.keys()))  # header

    fig = ff.create_table(cells, index=True)

    fig.show()
