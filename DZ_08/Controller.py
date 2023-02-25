import modul_view
import manager


def start():
    while True:
        choice = modul_view.menu()

        if choice == 1:
            manager.open_file()
            print('_________________________________________________ ')
            print('Файл телефонного справочника открыт.')
            print('_________________________________________________ ')
        elif choice == 2:
            manager.save_file()
            print('_________________________________________________ ')
            print('\nКонтакт сохранен!')
            print('_________________________________________________ ')
        elif choice == 3:
            print('_________________Список контактов________________ ')
            pb = manager.get()
            modul_view.show_contacts(pb)
            print('_________________________________________________ ')
        elif choice == 4:
            new = modul_view.new_contact_input()
            manager.add(new)
            print('_________________________________________________ ')
            print('\nКонтакт добавлен!')
            print('_________________________________________________ ')
        elif choice == 5:
            print('_________________Список контактов________________ ')
            modul_view.show_contacts(manager.get())
            print('_________________________________________________ ')
            ind = modul_view.input_id()
            print('_________________________________________________ ')
            contact = modul_view.new_contact_input()
            manager.change_contact(ind, contact)
            print('_______________Изменения внесены!________________ ')
        elif choice == 6:
            find = modul_view.find_contact()
            print('________________Результат поиска_________________ ')
            result = manager.find(find)
            modul_view.show_contacts(result)
            print('_________________________________________________ ')
            
        elif choice == 7:
            print('_________________Список контактов________________ ')
            modul_view.show_contacts(manager.get())
            print('_________________________________________________ ')
            ind = modul_view.input_id()
            manager.delete_contact(ind)
            print('_________________Контакт удалён!_________________ ')
        elif choice == 8:
            print('_________________________________________________ ')
            print('Программа завершила работу!\n')
            break

