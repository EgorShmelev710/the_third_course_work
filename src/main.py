from config import OPERATIONS_PATH
from functions import load_all_operations, filter_operations, sort_filtered_operations, transform_date, \
    hiding_requisites


def main():
    operations = load_all_operations(OPERATIONS_PATH)
    filtered_operations = filter_operations(operations)
    sorted_operations = sort_filtered_operations(filtered_operations)
    for operation in sorted_operations:
        print(f"{transform_date(operation['date'])} {operation['description']}")
        print(f"{hiding_requisites(operation, 'from')} -> {hiding_requisites(operation, 'to')}")
        print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")


main()
