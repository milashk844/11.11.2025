import pytest
from password import is_strong_password

def test_is_strong_password():
    password = 'Adfg657h'
    expected_result = True
    actual_result = is_strong_password(password=password)
    assert expected_result == actual_result
