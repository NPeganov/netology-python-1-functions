from globals import directories


def get_shelf_by_doc_number(doc_number):
    for shelf_number, documents in directories.items():
        if doc_number in documents:
            return shelf_number

    return None


def read_shelf(shelf):
    return directories.get(shelf)


def create_shelf(shelf):
    if not read_shelf(shelf):
        directories[shelf] = list()
        return directories.get(shelf)
    else:
        return None # shelf already exists


def put_doc_on_shelf(shelf_num, doc_num):
    shelf = read_shelf(shelf_num)
    if shelf:
        shelf.append(doc_num)
        return shelf
    else:
        #   new_shelf = create_shelf(shelf_num)
        #   new_shelf.append(doc_num)
        #   return new_shelf
        return shelf


def move_doc(doc_num, new_shelf):
    current_shelf_num = get_shelf_by_doc_number(doc_num)
    current_shelf = directories.get(current_shelf_num)
    new_shelf_docs = put_doc_on_shelf(new_shelf, doc_num)
    if new_shelf_docs:
        current_shelf.remove(doc_num)

    return new_shelf_docs
