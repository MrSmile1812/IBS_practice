import pytest

from task_7.chain_sum import chain_sum


@pytest.fixture
def numbers():
    a = 1
    b = 25
    c = 30
    d = -5
    e = 77
    return [a, b, c, d, e]


class TestChainSum:
    """Проведем тестирование с одним аргументом.
    С положительным и отрицательным аргументами.
    С множеством элементов"""
    def test_one_argument(self, numbers):
        res = chain_sum(numbers[2])()
        assert res == numbers[2]

    def test_negative_argument(self, numbers):
        res = chain_sum(numbers[3])(numbers[2])()
        assert res == numbers[1]

    def test_multiple_arguments(self, numbers):
        res = chain_sum(numbers[1])(numbers[0])(numbers[3])(numbers[2])(numbers[1])(numbers[0])()
        assert res == numbers[4]
