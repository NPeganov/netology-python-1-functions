from global_variables import *
from constants import *
import logging


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

def select_document(where):
    if not isinstance(where, dict):
        logging.error('A dict expected.')
    else:
        result = list()
        for key, value in where.items():
            for document in documents:
                if document[key] == value:
                    for shelf, docs in directories.items():
                        if document[K_NUMBER] in docs:
                            document[K_SHELF] = shelf
                    result.append(document)
        if len(result) == 0:
            result = None
        return result


def create_document(num, name, type, shelf):
    if not select_document({K_NUMBER: num}):
        logging.warning('Document with such number already exists')
    else:
        for document in documents:
            if document[K_NAME] == name and document[K_TYPE] == type:
                logging.warning('This person already has such document')
            else:
                break
        new_doc = dict()
        new_doc[K_TYPE] = type
        new_doc[K_NAME] = name
        new_doc[K_NUMBER] = num
        documents.append(new_doc)
        directories[shelf].append(num)
        result = {K_TYPE: type,
                  K_NUMBER: num,
                  K_NAME: name,
                  K_SHELF: shelf}
        return result


def read_document(where):
    result = select_document(where)
    return result


def update_document(doc, where):
    if not isinstance(where, dict) or not isinstance(doc, str | int | float):
        logging.error('Different data type expected.')
    else:
        for key, value in where.items():
            if key == K_SHELF:
                for shelf, docs in directories.items():
                    if doc in docs:
                        docs.remove(doc)
                    if shelf == key:
                        directories[docs].append(doc)
            elif key in [K_TYPE, K_NUMBER, K_NAME]:
                for document in documents:
                    if key == K_TYPE:
                        documents[document][K_TYPE] = value
                    elif key == K_NUMBER:
                        if value == document[K_NUMBER]:
                            logging.error('Such document already exists')
                        else:
                            documents[document][K_NUMBER] = value
                    else:
                        documents[document][K_NAME] = value
        return select_document({K_NUMBER: doc})


def delete_document(num):
    if not select_document({K_NUMBER: num}):
        logging.error('This document doesn`t exist')
    else:
        for document in documents:
            if document[K_NUMBER] == num:
                documents.remove(document)
            for d in directories.values():
                if num in d:
                    d.remove(num)
        return num
