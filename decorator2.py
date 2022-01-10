import datetime

def logger_decor2(path_to_logs):
    def _logger_decor2(old_function):
        def new_function(*args, **kwargs):   
            file_path = path_to_logs       
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
    return _logger_decor2


    