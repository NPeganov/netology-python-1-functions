from globals import *
from shelf import *


class DocKeys:
    NUMBER = 'number'
    OWNER = 'name'
    TYPE = 'type'
    SHELF = 'shelf'

def select_documents(where=dict()):
    """Возвращает массив tupple(shelf_number, document) """
    result = list()

    for document in documents:
        match_criteria_count = 0
        shelf_number = get_shelf_by_doc_number(document.get(DocKeys.NUMBER))
        for key, value in where.items():
            if key == DocKeys.SHELF:
                if value is not None and shelf_number == value:
                    match_criteria_count += 1
            else:
                if value is not None and value == document.get(key):
                    match_criteria_count += 1

        if match_criteria_count == len(where.items()):
            result.append((shelf_number, document))

    return result


def create_document(new_doc_dict):
    new_doc_num = new_doc_dict.get(DocKeys.NUMBER)
    doc_shelf = new_doc_dict.get(DocKeys.SHELF)
    if len(select_documents({DocKeys.NUMBER: new_doc_num})) == 0:
        shelf = read_shelf(doc_shelf)
        if shelf:
            put_doc_on_shelf(doc_shelf, new_doc_num)
        else:
            pass
            # Полка не найдена
            # или выходим с ошибкой
            # return ERROR
            # или создаём новыю полку и продолжаем
            # create_shelf(doc_shelf)

        documents.append({DocKeys.NUMBER: new_doc_num,
                          DocKeys.OWNER: new_doc_dict.get(DocKeys.OWNER),
                          DocKeys.TYPE: new_doc_dict.get(DocKeys.TYPE)})

        # return OK
    else:
        pass
        # Документ с таким номером существует - выходим с ошибкой
        # return ERROR


def read_documents(where=dict()):
    result = list()
    docs = select_documents(where)
    for shelf, doc in docs:
        doc_to_return = doc.copy()
        doc_to_return[DocKeys.SHELF] = shelf
        result.append(doc_to_return)

    return result


def update_document(doc_num, new_values):
    doc_to_update = select_documents({DocKeys.NUMBER: doc_num})
    if doc_to_update:
        shelf_to_return, doc_to_update = doc_to_update[0]
        for key, new_value in new_values.items():
            if key == DocKeys.SHELF:
                shelf_to_return = move_doc(doc_num=doc_num, new_shelf=new_value)
                if shelf_to_return is not None:
                    shelf_to_return = new_value
            else:
                if key in doc_to_update.keys():
                    doc_to_update[key] = new_value

        if shelf_to_return:
            doc_to_return = doc_to_update.copy()
            doc_to_return[DocKeys.SHELF] = shelf_to_return
            return doc_to_return

    return None


def delete_document(where=dict()):
    docs_to_delete = select_documents(where)
    removed_doc_nums = list()
    for shelf, document in docs_to_delete:
        doc_num = document.get(DocKeys.NUMBER)
        documents.remove(document)
        directories.get(shelf).remove(doc_num)
        removed_doc_nums.append(doc_num)

    return removed_doc_nums
