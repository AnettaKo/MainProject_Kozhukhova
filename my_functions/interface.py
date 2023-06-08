from my_functions.files import write_file
from my_functions.reports import *


def choose_action(menu):
    print("Choose action!")
    if menu == 'main menu':
        action = input("1 - Work with articles, 2 - Work with storages, 3 - Report, 0 - Exit: ")
    elif menu == 'articles':
        action = input('1 - Add new article, 2 - Change article, 3 - Delete article, 9 - Main menu, 0 - Exit: ')
    elif menu == 'storages':
        action = input('1 - Add new storage, 2 - Move storage, 3 - Delete storage 9 - Main menu, 0 - Exit: ')
    elif menu == 'reports':
        action = input('1 - Full table report, 9 - Maim menu,0 - Exit: ')
    return action


def main_menu(my_wardrobe):
    while True:
        action = choose_action('main menu')
        if action == '1':
            work_with_articles(my_wardrobe)
        elif action == '2':
            choose_action('storages')
        elif action == '3':
            work_with_reports(my_wardrobe)
        elif action == '0':
            exit_system(my_wardrobe)
        else:
            print("Incorrect answer")


def work_with_articles(my_wardrobe):
    while True:
        action = choose_action('articles')
        if action == '1':
            my_wardrobe.add_new_item()
        elif action == '2':
            my_wardrobe.change_item()
        elif action == '3':
            my_wardrobe.delete_item()
        elif action == '9':
            main_menu(my_wardrobe)
        elif action == '0':
            exit_system(my_wardrobe)
        else:
            print("Incorrect answer")

def work_with_reports(my_wardrobe):
    while True:
        action = choose_action('reports')
        if action == '1':
            full_table(my_wardrobe)
        elif action == '9':
            main_menu(my_wardrobe)
        elif action == '0':
            exit_system(my_wardrobe)
        else:
            print("Incorrect answer")


def exit_system(my_wardrobe):
    answer = input("Save changes made in session? Yes - 1, No - any other key: ")
    if answer == "1":
        write_file("wardrobe.csv", my_wardrobe)

    print("Good by!")
    raise SystemExit
