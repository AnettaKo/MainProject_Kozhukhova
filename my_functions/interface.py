
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


def main_menu(my_wardrobe):
    while True:
        action = choose_action('main menu')
        if action == '1':
            work_with_articles(my_wardrobe)
        elif action == '2':
            choose_action('storages')
        elif action == '3':
            choose_action('reports')
        elif action == '0':
            exit_system()
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
            exit_system()
        else:
            print("Incorrect answer")


def exit_system():
    print("Good by!")
    raise SystemExit
