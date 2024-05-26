import pytest
import json
from project import validate, save, load

SAVED_DATA = "clipvault_test.json"

def test_validate():
    assert validate("test", "test") is False
    assert validate("test", "test1") is True
    assert validate("test", " ") is False
    assert validate("", "test") is True


def test_save():
    test_data = ["data1", "data2", "data3"]
    assert save(SAVED_DATA, test_data) is True
    loaded_data = load(SAVED_DATA)
    assert loaded_data == test_data


def test_load():
    non_existent_file = "non_existent_file.json"
    assert load(non_existent_file) == []


if __name__ == "__main__":
    pytest.main()
