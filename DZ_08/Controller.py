import modul_view
import manager


def start():
    while True:
        choice = modul_view.menu()

        if choice == 1:
            manager.open_file()
            print('Файл телефонного справочника открыт.')

        elif choice == 2:
            manager.save_file()
            print('\nКонтакт сохранен!')

        elif choice == 3:
            print('________________Список контактов_______________ ')
            pb = manager.get()
            modul_view.show_contacts(pb)
            
        elif choice == 4:
            new = modul_view.new_contact_input()
            manager.add(new)
            print('\nКонтакт добавлен!')

        # elif choice == 5:

        # elif choice == 6:

        # elif choice == 7:

        elif choice == 8:
            print('Досвидания!')
            break

