from global_variables import *
import logging


def select_shelf(*shelves):
    result = list()
    for shelf in shelves:
        if shelf in directories.keys():
            result.append(shelf)
    if len(result) == 0:
        result = None
    return result


def create_shelf():
    pass


def read_shelf():
    pass


def update_shelf(**changes):
    result = None
    for current, changed in changes.items():
        for key in directories.keys():
            if current == key:
                key = changed
            result = key
    return result


print(update_shelf(text='4'))


def delete_shelf():
    pass
