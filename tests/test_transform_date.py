from src.functions import transform_date


def test_transform_date():
    assert transform_date("2018-04-14T19:35:28.978265") == "14.04.2018"
    assert transform_date("2019-08-26T10:50:58.294041") == "26.08.2019"
