from global_variables import directories
import logging


def find_directories(num):
    result = None
    for shelf in directories:
        if num in shelf or num in shelf.values():
            result = shelf
    return result


def create_shelf(new_num):
    for shelf in directories:
        if new_num in shelf:
            logging.error("The shelf already exists")
    directories[new_num] = []


def read_shelf(num):
    shelf = find_directories(num)
    return shelf


def update_shelf(new_num, shelf):
    if new_num in directories[shelf]:
        logging.error("The document is already on the shelf")
    directories[shelf].append(new_num)


def delete_shelf(num):
    if directories[num] != []:
        logging.critical("There are some documents on the shelf. Delete (d) or move (m) them, before deleting the shelf")
    else:
        del directories[num]
