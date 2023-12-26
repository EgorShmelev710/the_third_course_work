from src.functions import filter_operations


def test_filter_operations():
    operations = [
        {
            'id': '456456456465',
            'state': 'EXECUTED'
        },
        {
            'id': '123123123',
            'state': 'CANCELED'
        },
        {
            'id': '987987987',
            'state': 'EXECUTED'
        },
    ]
    expected = [
        {
            'id': '456456456465',
            'state': 'EXECUTED'
        },
        {
            'id': '987987987',
            'state': 'EXECUTED'
        },
    ]
    assert filter_operations(operations) == expected
