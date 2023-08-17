from enum import enum


documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

[{'shelf': '2', 'doc': {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}}]

{'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов', 'shelf': '2'}

ERR_CODES = enum.enum
(err_code, result)

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}
