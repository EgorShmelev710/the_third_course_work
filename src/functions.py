import json


def load_all_operations(path):
    with open(path, encoding='utf-8') as file:
        operations = json.load(file)
        return operations


def filter_operations(path):
    executed_operations = []
    for operation in path:
        if operation.get('state') == 'EXECUTED':
            executed_operations.append(operation)
    return executed_operations


def sort_filtered_operations(path):
    """
    функция выдает 5 последних совершенных операций
    """
    result = sorted(path, key=lambda path: path['date'], reverse=True)
    return result[:5]


def transform_date(old_date):
    date_splitter = old_date.split('T')
    date = date_splitter[0]
    date_parts = date.split('-')
    reversed_parts = reversed(date_parts)
    new_date = '.'.join(reversed_parts)
    return new_date


def hiding_requisites(operation, way):
    requisites = operation.get(way)
    if requisites is not None:
        parts = requisites.split()
        number = parts[-1]
        if requisites.lower().startswith('счет'):
            hidden_number = f"**{number[-4:]}"
        else:
            hidden_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
        parts[-1] = hidden_number
        return (' '.join(parts))
    return 'Unknown Source'
