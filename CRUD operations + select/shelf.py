from global_variables import *
import logging
import copy
import traceback


def _select_shelf(*shelves):
    result = list()
    for shelf in shelves:
        if shelf in directories:
            result.append(shelf)
    if len(result) == 0:
        result = None
    return result


def _select_shelf_by_doc(*docs):
    result = list()
    for doc in docs:
        for shelf in directories:
            if doc in directories[shelf]:
                result.append(shelf)
    return result


def create_shelf(*nums):
    result = dict.fromkeys(nums)
    for num in nums:
        if _select_shelf(num) is not None:
            logging.error("The shelf already exists")
        else:
            directories[num] = []
            result[num] = num
    # результат: {<и так существовавшая полка>: None,
    #             <новая полка>: <новая полка>}
    #
    # or:
    # result = list()
    # for num in nums:
    #     if _select_shelf(num) is not None:
    #         logging.error("The shelf already exists")
    #     else:
    #         directories[num] = []
    #         result.append(num)
    # результат: [<новая полка 1>, <новая полка 2>]
    # P.s. массив, содержащий только добавленные полки

    return result


def read_shelf(*shelves):
    return copy.deepcopy(_select_shelf(shelves))


def update_shelf(changes):
    u"""expects a dict <shelf to rename>: <new number>"""
    # if not isinstance(changes, dict):
    #     logging.error('Dictionary expected')
    try:
        # Создаём словарь с ключами соответствующими ключам входного словаря (полки)
        result = dict.fromkeys(changes.values())
        for current_shelf_number, new_shelf_number in changes.items():
            if _select_shelf(current_shelf_number) is None:
                logging.error(f'This shelf ({current_shelf_number}) doesn`t exist')
            elif _select_shelf(new_shelf_number) is not None:
                logging.error(f'This shelf ({new_shelf_number}) already exists')
            else:
                # Меняем полку
                directories[new_shelf_number] = directories.pop(current_shelf_number)
                # Добавляем значение там, где в общем то всё успешно
                result[new_shelf_number] = directories[new_shelf_number]
        return result
    except TypeError:
        print('Dictionary expected', traceback.print_exc())


def delete_shelf(*nums):
    result = dict.fromkeys(nums)
    for num in nums:
        if _select_shelf(num) is None:
            logging.error('The shelf doesn`t exist')
        elif directories[num]:
            logging.warning(
                "There are some documents on the shelf. Delete (d) or move (m) them, before deleting the shelf."
                "\nP.s. You can see which documents are on the shelf (l).")
        else:
            del directories[num]
            result[num] = num
        #     результат: {<несуществующая полка>: None,
        #                 <удалённая полка>, <удалённая полка>}
        #
        # or:
        #     del directories[num]
        #     result.append(num)
        #
        #  результат: [<удалённая полка 1>, <удалённая полка 2>]
        #  P.s. массив, содержащий только удалённые полки

            return result
