# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, 
# которые должны находиться в файле. 
# 1. Программа должна выводить данные 
# 2. Программа должна сохранять данные в текстовом файле 
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека) 
# 4. Использование функций. Ваша программа не должна быть линейной

from csv import DictReader, DictWriter
from os.path import exists


def get_info():
    is_valid_first_name = False
    while not is_valid_first_name:
        first_name = str(input('Введите имя: '))
        if len(first_name) < 2:
            print('Невалидное имя! ')
            continue
        elif first_name.isalpha() == False:
            print('Имя должно состоять только из букв! ')
        else:
            is_valid_first_name = True
    
    is_valid_last_name = False
    while not is_valid_last_name:       
        last_name = str(input('Введите фамилию: '))
        if len(last_name) < 2:
            print('Невалидная Фамилия! ')
            continue
        elif last_name.isalpha() == False:
            print('Фамилия должна состоять только из букв! ')
        else:
            is_valid_last_name = True

    is_valid_namber = False
    while not is_valid_namber:
        phone_namber = int(input('введите номер телефона: '))
        if len(str(phone_namber)) != 3:
            print('Невалидная длина! ')
            continue
        else:
            is_valid_namber = True
    return [first_name,last_name,phone_namber]


def creat_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_writer.writeheader()

def read_fale(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)
    
def write_fale(file_name):
    res = read_fale(file_name)
    user_data = get_info()
    for el in res:
        if el['телефон'] == str(user_data[2]):
            print('Такой пользователь уже сушествует!')
            return
    obj = {'имя':user_data[0], 'фамилия': user_data[1], 'телефон': user_data[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

file_name = 'phone.csv'

def main():
    while True:
        command = input('введите команду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                creat_file(file_name)
            write_fale(file_name)
        elif command == 'r':
            if not exists(file_name):
                print('файл не создан. Создайте его!')
                continue
            for el in read_fale(file_name):
                print(el)

main()

