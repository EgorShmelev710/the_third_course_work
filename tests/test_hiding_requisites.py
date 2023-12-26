from src.functions import hiding_requisites


def test_hiding_requisites_way():
    operation = {
        "id": 441945886,
        "from": "Maestro 1596837868705199"
    }

    expected = "Maestro 1596 83** **** 5199"
    assert hiding_requisites(operation, 'from') == expected


def test_hiding_requisites_way2():
    operation = {
        "id": 142264268,
        "from": "Счет 19708645243227258542"
    }

    expected = "Счет **8542"
    assert hiding_requisites(operation, 'from') == expected


def test_hiding_requisites_way3():
    operation = {
        "id": 142264268,
        "to": "Счет 75651667383060284188"
    }

    expected = "Счет **4188"
    assert hiding_requisites(operation, 'to') == expected
