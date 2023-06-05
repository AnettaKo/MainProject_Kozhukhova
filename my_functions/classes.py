from my_functions.interface import main_menu
from my_functions.classificators import *


class Storage:  # места хранения
    def __init__(self, name, storage_place, description: str):
        self.description = description
        self.storage_place = storage_place
        self.__name = name


class Item:

    def __init__(self, name, item_class=None, item_type=None, size=None, season=None, color=None,
                 brand=None, storage=None, price=0, description=""):
        # ,purchase_place,condition: condition_types):

        self.__name = name
        self.item_class = item_class or input_from_classificator(item_classes, "item_class")
        self.item_type = item_type or input_from_classificator(item_types.get(self.item_class), "item_type")
        self.size = size or self.input_size("size")
        self.season = season or input_from_classificator(seasons, "season")
        self.color = color or input_from_classificator(colors, "color")
        self.brand = brand or self.input_brand("brand")
        self.storage = storage or None
        self.price = price or self.input_price("price")
        self.description = description or input('description = ')
        # self.purchase_place = purchase_place
        # self.condition = condition

        self.price = float(self.price)  # if input from file

    def __eq__(self, other):
        return self.__name == other.__name

    def __str__(self):
        return str(self.__name)

    def fullstr(self):
        return str(self.__name) + ", " + str(self.item_class) + ", " + str(self.item_type) + ", " + str(self.size) \
            + ", " + str(self.season) + ", " + str(self.color) + ", " + str(self.brand) + ", " + str(self.storage) \
            + ", " + str(self.price) + ", " + str(self.description)

    def name(self):
        return self.__name

    @classmethod
    def input_name(cls):
        while True:
            name = input('Name = ')
            if name == '':
                print('Name cannot be empty')
            else:
                return name

    def change_article(self, my_wardrobe):
        print(f'article = {self.fullstr()}')
        attributes = list(self.__dict__.keys())
        attribute = input_from_classificator(attributes, 'attribute')
        print(f'old {attribute} = {self.__getattribute__(attribute)}')
        if attribute == "_Item__name":
            name = Item.input_name()
            article = my_wardrobe.find_item(name, True)
            if article is None:
                self.__name = name
            # else:
            #     print(f'Article with name {name} already exist.')
        elif attribute == 'item_class':
            self.item_class = input_from_classificator(item_classes, 'new item_class')
            self.item_type = input_from_classificator(item_types.get(self.item_class), 'new item type')
        elif attribute == 'item_tipe':
            self.item_type = input_from_classificator(item_types.get(self.item_class), 'new item type')
        elif attribute == 'size':
            self.size = self.input_size('new size')
        elif attribute == 'season':
            self.season = input_from_classificator(seasons, 'new season')
        elif attribute == 'color':
            self.color = input_from_classificator(colors, "new color")
        elif attribute == 'brand':
            self.brand = self.input_brand("new brand")
        elif attribute == 'price':
            self.price = self.input_price("new price")
        else:
            self.__setattr__(attribute, input(f'new {attribute} = '))

        action = input("Change other attribute? Yes - 1, No - 0: ")
        if action == '1':
            self.change_article(my_wardrobe)

    def input_size(self, attribute_name: str):
        if self.item_class in ['closes', 'shoes']:
            return input_from_classificator(sizes.get(self.item_class), attribute_name)
        else:
            return input(f'{attribute_name} = ')

    def input_brand(self, attribute_name: str):
        if self.item_class in ['closes', 'shoes']:
            brand = input_from_classificator(brands.get(self.item_class), attribute_name)
            if brand == 'input other':
                return input(f'{attribute_name} = ')
        else:
            return input(f'{attribute_name} = ')

    @classmethod
    def input_price(cls, attribute_name: str):
        while True:
            price = input(f'{attribute_name} = ')
            try:
                price = float(price)
                return price
            except:
                print("Incorrect price! Value must be float.")


class Wardrobe:
    def __init__(self, list_items: [Item]):
        self.__list_items = list_items

    def __str__(self):
        wardrobe_string = "My wardrobe:"
        index = 0
        for element in self.__list_items:
            index += 1
            wardrobe_string += "\n" + str(index) + ' ' + element.fullstr()
        return wardrobe_string

    def list_item(self):
        return self.__list_items

    def add_new_item(self):
        name = Item.input_name()
        new_article = self.find_item(name, True)
        if new_article is None:
            new_article = Item(name)
            self.__list_items.append(new_article)
        print(self)

    def find_item(self, name, new_item=False):
        for article in self.__list_items:
            if article.name() == name:
                if new_item:
                    print(f'Article with name "{name}" already exist.')
                return article
        if not new_item:
            print(f'Article with name "{name}" not found')
        return None

    def change_item(self):
        print("Choose action!")
        action = input('1 - Find article by name, 2 - Choose article from list, 9 - Main menu: ')
        if action == "1":
            name = Item.input_name()
            element = self.find_item(name)
            if element is None:
                self.change_item()
            else:
                element.change_article(self)
        elif action == '2':
            element = input_from_classificator(self.__list_items, 'article')
            element.change_article(self)
        elif action == '9':
            main_menu(self)
        else:
            print("Incorrect input")
            self.change_item()
        print(self)

    def delete_item(self):
        element = input_from_classificator(self.__list_items, 'article')
        answer = input("Do you really wont to delete element? Yes - 1, No - 0: ")
        if answer == "1":
            self.__list_items.remove(element)
        print(self)
