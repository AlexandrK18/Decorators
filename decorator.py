import os
import datetime
def logger_decor(old_function):
    def new_function(*args, **kwargs):
        file_path = f'{os.path.join(os.path.join(os.getcwd(), str(old_function.__name__)))}.txt'
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f'Дата и время вызова функции: {datetime.datetime.now()}\n')
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f'Вызвана функция: {old_function.__name__}\n')
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f'С аргументами: {args} и {kwargs}\n')
        result = old_function(*args, **kwargs)
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f'{result}\n')
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f'{"-"*120}\n')   
        return result
    return new_function 