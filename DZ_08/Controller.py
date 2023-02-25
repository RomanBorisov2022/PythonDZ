import modul_view
import manager


def start():
    while True:
        choice = modul_view.menu()

        if choice == 1:
            manager.open_file()
        # elif user_input == 2:

        elif choice == 3:
            pb = manager.get()
            modul_view.show_contacts(pb)

        elif choice == 4:
            new = modul_view.new_contact_input()
            manager.add(new)

        # elif choice == 5:

        # elif choice == 6:

        # elif choice == 7:

        elif choice == 8:
            print('Досвидания!')
            break

