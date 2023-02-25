

def menu():
    print('''\n______________Выберите пункт меню:______________
        1. Открыть файл
        2. Сохранить файл
        3. Показать контакты
        4. Создать контакт
        5. Изменить контакт
        6. Найти контакт
        7. Удалить  контакт
        8. Выход''')
    choice = int(input('Введите данные: '))
    return choice


def show_contacts(pb: list[dict]):
    if pb == []:
        print('Телефонная книга пуста или файл не открыт!')
    else:
        for i, contact in enumerate(pb, 1):
            name = contact.get('name')
            phone = contact.get('phone')
            comment = contact.get('comment')
            print(f'{i}. {name:<20} {phone:<15} {comment:<20}')

def new_contact_input():
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    new_contact = {'name': name,
                   'phone':  phone,
                   'comment': comment}
    return new_contact

def find_contact():
    find = input('Введите искомый элемент: ')
    return find