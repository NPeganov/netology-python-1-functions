from global_variables import *
from constants import K_NUMBER, K_NAME, K_TYPE, KEYS
import logging


def find_document(key, value):
    result = None
    for dict in documents:
        for a in dict:
            if dict[key] == value:
                result = dict
    #             result = a
    return result


def create_document(doc_type, num, owner_name):
    for d in documents:
        for _ in d:
            if num in _:
                logging.critical("The document already exists")
    document = dict()
    document[K_TYPE] = doc_type
    document[K_NUMBER] = num
    document[K_NAME] = owner_name
    documents.append(document)


def read_document(key, value):
    document = find_document(key, value)
    return document


def update_document(doc_num, **document_info):
    if not document_info.keys() in KEYS:
        logging.critical("Wrong key(s)")
    document = find_document('name', doc_num)
    for key, value in document_info.items():
        document[key] = value


def delete_document(num):
    for document in documents:
        if document[K_NUMBER] == num:
            documents.remove(document)
        # for d in directories.values():
        #     if num in d:
        #         d.remove(num)
