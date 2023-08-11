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
def select_document(**info):
    result = list
    for key, value in info.items():
        if key == K_SHELF:
            result += directories[key]




def create_document():
    pass


def read_document():
    pass


def update_document():
    pass


def delete_document():
    pass
