# from flask import Flask

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint

my_wardrobe = 'global variable'


def choose_action(menu):
    print("Choose action!")
    if menu == 'main menu':
        action = input("1 - Work with articles, 2 - Work with storages, 3 - Report, 0 - Exit: ")
    elif menu == 'articles':
        action = input('1 - Add new article, 2 - Change article, 3 - Delete article, 9 - Main menu, 0 - Exit: ')
    elif menu == 'storages':
        action = input('1 - Add new storage, 2 - Move storage, 3 - Delete storage 9 - Main menu, 0 - Exit: ')
    elif menu == 'reports':
        action = input('1 - Article report, 2 - Storage report, 9 - Maim menu,0 - Exit: ')
    return action


def main_menu():
    while True:
        action = choose_action('main menu')
        if action == '1':
            work_with_articles()
        elif action == '2':
            choose_action('storages')
        elif action == '3':
            choose_action('reports')
        elif action == '0':
            exit_sysytem()
        else:
            print("Incorrect answer")


def work_with_articles():
    while True:
        action = choose_action('articles')
        if action == '1':
            my_wardrobe.add_new_item()
        elif action == '2':
            my_wardrobe.change_item()
        elif action == '3':
            my_wardrobe.delete_item()
        elif action == '9':
            main_menu()
        elif action == '0':
            exit_sysytem()
        else:
            print("Incorrect answer")


def exit_sysytem():
    print("Good by!")
    raise SystemExit


def input_from_classificator(classificator: list, attribute_name: str):
    print("Choose " + attribute_name + "!")

    text = ""
    index = 0
    for element in classificator:
        text += str(index) + " - " + str(element) + ", "
        index += 1

    correct_input = False
    while not correct_input:
        action = input(f'{text} :')
        try:
            action = int(action)
            if action < len(classificator):
                element = classificator[action]
                correct_input = True
                print(f"{attribute_name} = {element}")
            else:
                print("Incorrect answer")
        except:
            print("Incorrect answer")

    return element


seasons = ['summer', 'demi', 'winter', None]
condition_types = ['new', 'good', 'bed', 'spoiled', 'required repair']
item_classes = ['closes', 'shoes', 'accessories', 'other']
item_types = {'closes': ['pant', 'jeans', 'pullover', 'suit', 't-shirt', 'shirt', 'jacket', 'overall', 'hat', 'mittens',
                         'socks', 'underpants', 'pajamas', 'other'],
              'shoes': ['snickers', 'slippers', 'boots', 'sandals', 'clogs', 'high boots', 'rain boots', 'other'],
              'accessories': ['glasses', 'bag', 'headgear', 'other'],
              'other': 'other'}
colors = ['red', 'yellow', 'green', 'blue', 'white', 'black', 'multicolor', 'printed', 'brown', 'grey', 'pink',
          'orange', 'turquoise']
sizes = {'closes': ['98', '104', '110', '116', '98-104', '104-110', '110-116', '3T', '4T', '5T'],
         'shoes': ['25', '26', '27', '28', 'C9', 'C10', 'C11']}
brands = {'closes': ['lupilu', 'kik', 'H&M', 'C&A', 'carters', 'childrens place', 'input other'],
          'shoes': ['elefanten', 'kik', 'crocs', 'ecco', 'input other']}


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
        self.size = size or self.input_size()
        self.season = season or input_from_classificator(seasons, "season")
        self.color = color or input_from_classificator(colors, "color")
        self.brand = brand or self.input_brand()
        self.storage = storage or None
        self.price = price or self.input_price()
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

    def change_article(self):
        attributes = list(self.__dict__.keys())
        attribute = input_from_classificator(attributes, 'attribute')
        print(attribute)
        if attribute == "Item__name":
            pass
        elif attribute == 'item_class':
            pass
        elif attribute == 'item_tipe':
            pass
        elif attribute == 'size':
            self.size = self.input_size()
        elif attribute == 'season':
            self.season = input_from_classificator(seasons,'season')
        elif attribute == 'color':
            self.color = input_from_classificator(colors, "color")
        elif attribute == 'brand':
            self.brand = self.input_brand()
        elif attribute == 'price':
            self.price = self.input_price()
        else:
            pass
            #self[attribute] = input(f'{attribute} = ')

    def input_size(self):
        if self.item_class in ['closes', 'shoes']:
            return input_from_classificator(sizes.get(self.item_class), "size")
        else:
            return input('size = ')

    def input_brand(self):
        if self.item_class in ['closes', 'shoes']:
            brand = input_from_classificator(brands.get(self.item_class), 'brand')
            if brand == 'input other':
                return input('brand = ')
        else:
            return input('brand = ')

    def input_price(self):
        while True:
            price = input("price = ")
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
        name = input('Name = ')
        new_article = self.find_item(name)
        if new_article is None:
            new_article = Item(name)
            self.__list_items.append(new_article)
        else:
            print(f'Article with name {name} already exist.')
            work_with_articles()
        print(self)

    def find_item(self, name):
        for article in self.__list_items:
            if article.name() == name:
                return article
        return None

    def change_item(self):
        element = input_from_classificator(self.__list_items, 'article')
        element.change_article()

    def delete_item(self):
        element = input_from_classificator(self.__list_items, 'article')
        answer = input("Do you really wont to delete element? Yes - 1, No - 0: ")
        if answer == "1":
            self.__list_items.remove(element)
        print(self)


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

    global my_wardrobe
    my_wardrobe = Wardrobe(list_items)
    print(my_wardrobe)


if __name__ == '__main__':
    read_file("wardrobe.csv")
    main_menu()

# app = Flask(__name__)
# @app.route("/")
# def hello_world():
#     return """
#     <p>Hello, World!</p>
#     <label for = "fname">Currency:</label>
#     <input type = "text" id = "fname" name = "fname"><br><br>
#         """
