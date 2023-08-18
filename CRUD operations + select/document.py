from global_variables import *
from constants import *
import logging
import copy
import traceback


# input:
# 1st parameter "where" as a dict in a form:
# {
#     "key1" : value1
#     "key2" : value2
#     ...
# }
# 2nd parameter as an enum: "and"/"or"
# alternatively: true/false
#
# Output: a list
#   [result_dict_1,
#   result_dict_2
#   ...]

def _select_document(where):
    # if not isinstance(where, dict):
    #     logging.error('A dict expected.')
    # else:
    try:
        result = list()
        result_from_dictionary = str()
        for key, value in where.items():
            for document in documents:
                if document[key] == value:
                    # Поиск нужного документа
                    for shelf, docs in directories.items():
                        # Формирование вывода
                        if document[KEY_NUMBER] in docs:
                            result_from_dictionary = shelf
                            break
                    result.append((document, {KEY_SHELF: result_from_dictionary}))
        if len(result) == 0:
            result = None
        return result
    except TypeError:
        print('A dict expected.', traceback.print_exc())


def create_document(num, name, type, shelf):
    if _select_document({KEY_NUMBER: num}) is None:
        logging.warning(f'Document with such number ({num}) already exists')
    else:
        # for document in documents:
        #     Не актуально
        #     if document[KEY_NAME] == name and document[KEY_TYPE] == type:
        #         logging.warning('This person already has such document')
        #     else:
        #         break
        new_doc = dict()
        # Добавление нового документа
        new_doc[KEY_TYPE] = type
        new_doc[KEY_NAME] = name
        new_doc[KEY_NUMBER] = num
        documents.append(new_doc)
        directories[shelf].append(num)
        result = {KEY_TYPE: type,
                  KEY_NUMBER: num,
                  KEY_NAME: name,
                  KEY_SHELF: shelf}
        return result


def read_document(where):
    document_tuple = copy.deepcopy(_select_document(where))[0]
    documents_info = document_tuple[0]
    directories_info = document_tuple[1]
    result = documents_info | directories_info
    return result


def update_document(doc, where):
    # if not isinstance(where, dict) or not isinstance(doc, str | int | float):
    #     logging.error('Different data type expected.')
    try:
        document = _select_document({KEY_NUMBER: doc})[0]
        result = list()
        for key, value in where.items():
            # Поиск нужного документа
            if key == KEY_SHELF:
                # Апдейтим полку
                for shelf, docs in directories.items():
                    if doc in docs:
                        # Сначала убираем со старой полки
                        docs.remove(doc)
                    if shelf == key:
                        # Добавляем на новую
                        directories[docs].append(doc)
                        result.append(doc)
            elif key == KEY_TYPE:
                document[0][KEY_TYPE] = value
                result.append(doc)
            elif key == KEY_NAME:
                document[0][KEY_NAME] = value
                result.append(doc)
            elif key == KEY_NUMBER:
                for doc in documents:
                    if value in doc[KEY_NUMBER]:
                        logging.error(f'Such document ({value}) already exists')
                        break
                document[0][KEY_NUMBER] = value
                for shelf, docs in directories.items():
                    if value in docs:
                        docs.remove(value)
                        docs.append(doc)
                        result.append(doc)
        return result

        # for key, value in where.items():
        #     # Поиск нужного документа
        #     if key == KEY_SHELF:
        #         # Апдейтим полку
        #         for shelf, docs in directories.items():
        #             if doc in docs:
        #                 # Сначала убираем со старой полки
        #                 docs.remove(doc)
        #             if shelf == key:
        #                 # Добавляем на новую
        #                 directories[docs].append(doc)
        #     elif key in [KEY_TYPE, KEY_NUMBER, KEY_NAME]:
        #         for document in documents:
        #             if key == KEY_TYPE:
        #                 # Апдейтим тип
        #                 documents[document][KEY_TYPE] = value
        #             elif key == KEY_NUMBER:
        #                 # Апдейтим номер
        #                 if value == document[KEY_NUMBER]:
        #                     logging.error(f'Such document ({value}) already exists')
        #                 else:
        #                     documents[document][KEY_NUMBER] = value
        #             else:
        #                 # Апдейтим владельца
        #                 documents[document][KEY_NAME] = value
        # return _select_document({KEY_NUMBER: doc})
    except TypeError:
        print('Different data type expected.', traceback.print_exc())


def delete_document(num):
    if _select_document({KEY_NUMBER: num}) is None:
        logging.error(f'This document ({num}) doesn`t exist')
    else:
        documents.remove(_select_document({KEY_NUMBER: num}))
        for d in directories.values():
            if num in d:
                d.remove(num)
        return num
