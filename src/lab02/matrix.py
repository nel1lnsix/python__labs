"""ЛР2, задание B — матрицы (списки списков)."""


def transpose(mat: list[list[float | int]]) -> list[list]:
    """Поменять местами строки и столбцы матрицы.

    Пустая матрица [] → [].

    Raises:
        ValueError: если матрица «рваная» (строки разной длины).
    """
    # TODO: твоё решение
    pass


def row_sums(mat: list[list[float | int]]) -> list[float]:
    """Вернуть список сумм по каждой строке.

    Raises:
        ValueError: если матрица «рваная».
    """
    # TODO: твоё решение
    pass


def col_sums(mat: list[list[float | int]]) -> list[float]:
    """Вернуть список сумм по каждому столбцу.

    Raises:
        ValueError: если матрица «рваная».
    """
    # TODO: твоё решение
    pass


if __name__ == "__main__":
    print("--- transpose ---")
    print(transpose([[1, 2, 3]]))          # [[1], [2], [3]]
    print(transpose([[1], [2], [3]]))      # [[1, 2, 3]]
    print(transpose([[1, 2], [3, 4]]))     # [[1, 3], [2, 4]]
    print(transpose([]))                   # []
    try:
        print(transpose([[1, 2], [3]]))
    except ValueError as e:
        print("ValueError:", e)            # ValueError: ...

    print("--- row_sums ---")
    print(row_sums([[1, 2, 3], [4, 5, 6]]))   # [6, 15]
    print(row_sums([[-1, 1], [10, -10]]))     # [0, 0]
    print(row_sums([[0, 0], [0, 0]]))         # [0, 0]
    try:
        print(row_sums([[1, 2], [3]]))
    except ValueError as e:
        print("ValueError:", e)               # ValueError: ...

    print("--- col_sums ---")
    print(col_sums([[1, 2, 3], [4, 5, 6]]))   # [5, 7, 9]
    print(col_sums([[-1, 1], [10, -10]]))     # [9, -9]
    print(col_sums([[0, 0], [0, 0]]))         # [0, 0]
    try:
        print(col_sums([[1, 2], [3]]))
    except ValueError as e:
        print("ValueError:", e)               # ValueError: ...
