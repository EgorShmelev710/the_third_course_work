import json
from config import OPERATIONS_PATH


def load_all_operations(path):
    with open(path, encoding='utf-8') as file:
        operations = json.load(file)
        return operations


operations = load_all_operations(OPERATIONS_PATH)


def filter_operations(path):
    executed_operations = []
    for operation in path:
        if operation.get('state') == 'EXECUTED':
            executed_operations.append(operation)
    return executed_operations
