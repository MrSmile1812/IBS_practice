def chain_sum(number: int):
    """Решим задачу с помощью рекурсивной функции"""
    result = number

    def recursion(number2: int = None):
        nonlocal result
        try:
            number2 = int(number2)
        except TypeError:
            return result
        result += number2
        return recursion

    return recursion


if __name__ == "__main__":
    print(chain_sum(5)())
    print(chain_sum(5)(2)())
    print(chain_sum(5)(100)(-10)())
    print(chain_sum(5)(100)(-10)(10)())
