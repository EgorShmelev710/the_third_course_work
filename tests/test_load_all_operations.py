import os
from src.functions import load_all_operations
from config import ROOT_DIR


def test_load_all_operations():
    DATA_PATH = os.path.join(ROOT_DIR, 'tests', 'operations_for_test.json')
    assert load_all_operations(DATA_PATH) == [1, 2, 3]
