from decorator import logger_decor

from decorator2 import logger_decor2

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }
      

# @logger_decor2('E:\Decorators\path_to_logs\info1.txt')
@logger_decor
def to_determine_owner_document(numbers):
  max_id = 99
  counter = 0
  for id, document in enumerate(documents):
    if numbers == document["number"]:
      max_id = id
      return f'Имя человека, которому принадлежит документ: {documents[max_id]["name"]}'
    elif numbers != document["number"]:
      counter += 1
      if counter == len(documents):
        return 'Введен несуществующий номер документа'

# @logger_decor2('E:\Decorators\path_to_logs\info2.txt')
@logger_decor
def to_determine_numder_shelves(numbers):
  counter = 0
  max_id = 99
  for id, shelve in enumerate(directories.values()):
    shelves_key = list(directories.keys())
    if numbers in shelve:
      max_id = id
      return f'Номер полки на которой находится документ: {shelves_key[max_id]}'
    elif numbers not in shelve:
      counter += 1
      if counter == len(directories):
        return 'Введен несуществующий номер документа' 


if __name__ == '__main__':

  to_determine_owner_document("2207 876234")

  to_determine_numder_shelves("2207 876234")

  to_determine_owner_document("11-2")

  to_determine_numder_shelves("11-2")

  to_determine_owner_document("10006")

  to_determine_numder_shelves("10006")