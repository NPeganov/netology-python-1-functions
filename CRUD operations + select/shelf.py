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


def create_shelf(*nums):
    for num in nums:
        if not select_shelf(num):
            logging.error("The shelf already exists")
        directories[num] = []


def read_shelf(*shelves):
    result = list()
    for shelf in shelves:
        if not select_shelf(shelf):
            logging.error('The shelf doesn`t exist')
        else:
            result.append(shelf)
    if len(result) == 0:
        result = None
    return result


def update_shelf(changes):
    u"""expects a dict <shelf to rename>: <new number>"""
    if not isinstance(changes, dict):
        logging.error('Dictionary expected')
    else:
        result = dict.fromkeys(changes.values(), 'unsuccessful')
        for current, changed in changes.items():
            if not select_shelf(current):
                logging.error('This shelf doesn`t exist')
            elif select_shelf(changed):
                logging.error('This shelf already exists')
            else:
                directories[changed] = directories.pop(current)
                result[changed] = directories[changed]
        return result


def delete_shelf(*nums):
    for num in nums:
        if not select_shelf(num):
            logging.error('The shelf doesn`t exist')
        elif directories[num]:
            logging.warning(
                "There are some documents on the shelf. Delete (d) or move (m) them, before deleting the shelf."
                "\nP.s. You can see which documents are on thr shelf (l).")
        else:
            del directories[num]


print(select_shelf('1', '2'))
