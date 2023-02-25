

def menu():
    print('''\nГлавное меню:
        1. Открыть файл
        2. Сохранить файл
        3. Показать контакты
        4. Создать контакт
        5. Изменить контакт
        6. Найти контакт
        7. Удалить  контакт
        8. Выход''')
    choice = int(input('Выберите пункт меню: '))
    return choice


def show_contacts(pb: list[dict]):
    if pb == []:
        print('Телефонная книга пуста или файл не открыт!')
    else:
        for i, contact in enumerate(pb, 1):
            first_name = contact.get(first_name)
            second_name = contact.get(second_name)
            phone = contact.get(phone)
            print(f'{i}. {first_name:<12} {second_name:<12} {phone:<15}')

def new_contact_input():
    first_name = input('Введите имя: ')
    second_name = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')
    new_contact = {'first_name': first_name,
                   'second_name':  second_name,
                   'phone': phone}
    return new_contact