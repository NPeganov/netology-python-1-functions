from global_variables import documents
from constants import *
import logging


def select_type(*types):
    result = list()
    for type in types:
        for document in documents:
            if document[K_TYPE] == type:
                result.append(document[K_TYPE])
    if len(result) == 0:
        result = None
    return result


def create_type():
    pass


def read_type():
    pass


def update_type():
    pass


def delete_type():
    pass
