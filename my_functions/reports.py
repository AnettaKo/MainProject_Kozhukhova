import plotly.graph_objs as go
import plotly.figure_factory as ff
from my_functions.classificators import *


def full_table(my_wardrobe):
    list_items = my_wardrobe.list_items()

    if len(list_items) == 0:
        print('no items in wardrobe')
        return

    cells = [list(item.__dict__.values()) for item in list_items]
    cells.insert(0, list(list_items[0].__dict__.keys()))  # header

    fig = ff.create_table(cells, index=True)

    # fig.update_layout(
    #     title_text='2016 Hockey Stats',
    #     margin={'t': 50, 'b': 100},
    #     # xaxis={'domain': [0, .5]},
    #     # xaxis2={'domain': [0.6, 1.]},
    #     # yaxis2={'anchor': 'x2', 'title': 'Goals'}
    # )
    fig.show()


def bar_prices(my_wardrobe):
    list_items = my_wardrobe.list_items()
    pass


def filtered_table(my_wardrobe):
    list_items = my_wardrobe.list_items()
    if len(list_items) == 0:
        print('no items in wardrobe')
        return

    selection = {}

    list_attributes = ['item_class', 'item_type', 'size', 'season', 'color', 'brand']
    list_attributes_selected = []

    add_attribute = True
    while add_attribute:
        # attributes = Item.header_attributes()
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

            answer = input(f'Do you wont to add new value of "{attribute}" to selection? Yes - 1, No - any other key: ')
            if answer != "1":
                add_value = False

        selection.update({attribute: list_values_selected})

        answer = input("Do you wont to add new attribute to selection? Yes - 1, No - any other key: ")
        if answer != "1":
            add_attribute = False

    print(selection)


# def select_items(my_wardrobe, selection):
#     list_items = my_wardrobe.list_items()
#
#     list_items_selected = list_items
#
#     for attribute in selection:
#         pass

