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
        first_name = str(input('Введите имя: ')).lower()
        if len(first_name) < 2:
            print('Невалидное имя! ')
            continue
        elif first_name.isalpha() == False:
            print('Имя должно состоять только из букв! ')
        else:
            is_valid_first_name = True
    
    is_valid_last_name = False
    while not is_valid_last_name:       
        last_name = str(input('Введите фамилию: ')).lower()
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
    
def write_fale(file_name, user_data):
    res = read_fale(file_name)
    if user_data == '':
        user_data = get_info()
        obj = {'Имя': user_data[0],
               'Фамилия': user_data[1], 'Телефон': user_data[2]}
    else:
        obj = user_data
    res.append(obj)
    if user_data == '':
        for el in res:
            if el['Телефон'] == str(user_data[2]):
                print('Пользователь уже существует')
                return
            
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)


def define_new_file_name():
    new_file_name = input('Введите файл куда скопировать данные ').lower()
    if exists(new_file_name) == True:
        return new_file_name
    else:
        request = str(input('Создать новый файл? да или нет: ')).lower()
        if request == 'да':
            creat_file(new_file_name)
            return new_file_name
        else:
            return ''


def copy_string(file_name, new_file_name):
    res = False
    if file_name == '' or new_file_name == '':
        print('Имя файла пустое')
    else:
        data = read_fale(file_name)
        while res == False:
            copy_string = int(input('Введите строку для копирования: '))
            if copy_string < 1 or copy_string >= len(data):
                print('Введите значение от 1 до ' + str(len(data)))
            else:
                write_fale(new_file_name, data[copy_string-1])
                res = True
    return res
        
file_name = 'phone.csv'

def main():
    print("список доступных команд ")
    print('\'r\'-вывод телефонного справочника в консоль')
    print('\'w\'-сохранить новый контак')
    print('\'с\'-скопировать контак из одного файла в другой')
    print('\'q\'-закрыть программу')
    print('\'h\'-вызов помощи')
    while True:
        command = input('введите команду: ').lower()
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
                print(f'{el["имя"]}, {el["фамилия"]}, {el["телефон"]}')
        elif command == 'h':
            print("список доступных команд ")
            print('\'r\'-вывод телефонного справочника в консоль')
            print('\'w\'-сохранить новый контак')
            print('\'с\'-скопировать контак из одного файла в другой')
            print('\'q\'-закрыть программу')
            print('\'h\'-вызов помощи')
        elif command == 'c':
            if copy_string(file_name, define_new_file_name()) == True:
                print('Строка скопирована')
            else:
                print('Скопировать строку не удалось')
        
main()