from dataclasses import dataclass

from my_functions.classificators import *


class Storage:  # места хранения
    def __init__(self, name, storage_place, description: str):
        self.description = description
        self.storage_place = storage_place
        self.__name = name


class Item:

    def __init__(self, _Item__name, item_class=None, item_type=None, size=None, season=None, color=None,
                 brand=None, storage=None, price: float = 0, description=None):

        self.__name = _Item__name
        self.item_class = item_class or input_from_classificator(item_classes, "item_class")
        self.item_type = item_type or input_from_classificator(item_types.get(self.item_class), "item_type")
        self.size = size or self.input_size("size")
        self.season = season or input_from_classificator(seasons, "season")
        self.color = color or input_from_classificator(colors, "color")
        self.brand = brand or self.input_brand("brand")
        self.storage = storage or None
        self.price = price or self.input_price("price")
        self.description = description or input('description = ').strip()

        if self.description == '':
            self.description = None
        # for attribute in self.__dict__.keys():
        #     attribute_value = self.__getattribute__(attribute)
        #     if attribute_value == "None" or attribute_value == "":
        #         self.__setattr__(attribute, None)
        #         if attribute == "price":
        #             self.price = 0

        self.price = float(self.price)  # if input from file

    def __eq__(self, other):
        return self.__name == other.__name

    def __str__(self):
        return self.__name

    def fullstr(self, delimiter="; "):
        return str(self.__name) + delimiter + str(self.item_class) + delimiter + str(self.item_type) + delimiter + str(
            self.size) \
            + delimiter + str(self.season) + delimiter + str(self.color) + delimiter + str(
                self.brand) + delimiter + str(self.storage) \
            + delimiter + str(self.price) + delimiter + str(self.description)

    def name(self):
        return self.__name

    @classmethod
    def header_attributes(cls):
        list_header = ['name', 'item_class', 'item_type', 'size', 'season', 'color', 'brand', 'storage', 'price',
                       'description']
        # print(list_header)
        return list_header

    @classmethod
    def input_name(cls):
        while True:
            name = input('Name = ').strip()
            if name == '':
                print('Name cannot be empty')
            else:
                return name

    # def input_new_item(self, name):
    #     item_class = input_from_classificator(item_classes, 'item_class')
    #     item_type = input_from_classificator(item_types.get(item_class), 'item type')
    #     size = self.input_size('size')
    #     season = input_from_classificator(seasons, 'season')
    #     color = input_from_classificator(colors, "color")
    #     brand = self.input_brand("brand")
    #     storage = input('storage = ').strip()
    #     price = self.input_price("price")
    #     description = input('description = ').strip()
    #
    #     new_Item = Item(name, item_class, item_type, size, season, color, brand, storage, price, description)
    #     return new_Item

    def change_article(self, my_wardrobe):
        print(f'article = {self.fullstr()}')
        attributes = list(self.__dict__.keys())
        # attributes = Item.header_attributes()
        attribute = input_from_classificator(attributes, 'attribute')
        print(f'old {attribute} = {self.__getattribute__(attribute)}')
        if attribute == "_Item__name":
            name = Item.input_name()
            article = my_wardrobe.find_item(name, True)
            if article is None:
                self.__name = name
        elif attribute == "item_class":
            item_class = input_from_classificator(item_classes, 'new item_class')
            if item_class != self.item_class:
                self.item_class = item_class
                self.item_type = input_from_classificator(item_types.get(item_class), 'new item type')
                self.size = self.input_size('new size')
                self.brand = self.input_brand('new brand')
        elif attribute == "item_type":
            self.item_type = input_from_classificator(item_types.get(self.item_class), 'new item type')
        elif attribute == "size":
            self.size = self.input_size('new size')
        elif attribute == "season":
            self.season = input_from_classificator(seasons, 'new season')
        elif attribute == "color":
            self.color = input_from_classificator(colors, "new color")
        elif attribute == "brand":
            self.brand = self.input_brand("new brand")
        elif attribute == "price":
            self.price = self.input_price("new price")
        else:
            new_value = input(f'new {attribute} = ').strip()
            if new_value == "" or new_value == "None":
                new_value = None
            self.__setattr__(attribute, new_value)

        action = input("Change other attribute? Yes - 1, No - any other key: ")
        if action == '1':
            self.change_article(my_wardrobe)

    def input_size(self, attribute_name: str):
        if self.item_class in ["closes", "shoes"]:
            return input_from_classificator(sizes.get(self.item_class), attribute_name)
        else:
            size = input(f'{attribute_name} = ').strip()
            if size == "":
                size = None
            return size

    def input_brand(self, attribute_name: str):
        if self.item_class in ["closes", "shoes"]:
            brand = input_from_classificator(brands.get(self.item_class), attribute_name)
            if not brand == "input other":
                return brand
        brand = input(f'{attribute_name} = ').strip()
        if brand == "":
            brand = None
        return brand

    @classmethod
    def input_price(cls, attribute_name: str):
        while True:
            price = input(f'{attribute_name} = ').strip()
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

    def list_items(self):
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

    def choose_item(self):
        print("Choose action!")
        action = input('1 - Find article by name, 2 - Choose article from list: ')
        if action == "1":
            name = Item.input_name()
            return self.find_item(name)
        elif action == '2':
            return input_from_classificator(self.__list_items, 'article')
        else:
            print("Incorrect input")
            return None

    def change_item(self):
        element = self.choose_item()
        if element is not None:
            element.change_article(self)

    def delete_item(self):
        element = self.choose_item()
        if element is not None:
            print(element.fullstr())
            answer = input("Do you really wont to delete element? Yes - 1, No - any other key: ")
            if answer == "1":
                self.__list_items.remove(element)
            print(self)
