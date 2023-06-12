from my_functions.files import read_file
from my_functions.interface import main_menu

if __name__ == '__main__':
    my_wardrobe = read_file("wardrobe.csv")
    main_menu(my_wardrobe)
