import pytest

from task_8.int_to_roman import int_to_roman


@pytest.fixture
def numbers():
    a = 187
    b = 1999
    c = 'CLXXXVII'
    d = 'MCMXCIX'
    return [a, b, c, d]


class TestIntToRoman:
    """Проведем тесты с различными числами."""
    def test_little_number(self, numbers):
        res = int_to_roman(numbers[0])
        assert res == numbers[2]

    def test_large_number(self, numbers):
        res = int_to_roman(numbers[1])
        assert res == numbers[3]
