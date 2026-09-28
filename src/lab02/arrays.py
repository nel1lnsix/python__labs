"""ЛР2, задание A — операции над списками."""


def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """Вернуть кортеж (минимум, максимум) из списка nums.

    Встроенные min() и max() использовать нельзя.

    Raises:
        ValueError: если список пуст.
    """
    # TODO: твоё решение
    pass


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """Вернуть отсортированный по возрастанию список уникальных значений.

    Встроенные sorted() и .sort() использовать нельзя.
    """
    # TODO: твоё решение
    pass


def flatten(mat: list[list | tuple]) -> list:
    """«Расплющить» список списков/кортежей в один список по строкам.

    Raises:
        TypeError: если какой-то элемент mat — не список и не кортеж.
    """
    # TODO: твоё решение
    pass


if __name__ == "__main__":
    # Этот блок выполняется только при запуске файла напрямую:
    # python src/lab02/arrays.py
    # Справа в комментарии — что должно получиться.

    print("--- min_max ---")
    print(min_max([3, -1, 5, 5, 0]))      # (-1, 5)
    print(min_max([42]))                  # (42, 42)
    print(min_max([-5, -2, -9]))          # (-9, -2)
    print(min_max([1.5, 2, 2.0, -3.1]))   # (-3.1, 2)
    # try/except ловит ошибку, чтобы программа не упала и пошла дальше
    try:
        print(min_max([]))
    except ValueError as e:
        print("ValueError:", e)           # ValueError: ...

    print("--- unique_sorted ---")
    print(unique_sorted([3, 1, 2, 1, 3]))         # [1, 2, 3]
    print(unique_sorted([]))                      # []
    print(unique_sorted([-1, -1, 0, 2, 2]))       # [-1, 0, 2]
    print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))   # [0, 1.0, 2.5]

    print("--- flatten ---")
    print(flatten([[1, 2], [3, 4]]))         # [1, 2, 3, 4]
    print(flatten([[1, 2], (3, 4, 5)]))      # [1, 2, 3, 4, 5]
    print(flatten([[1], [], [2, 3]]))        # [1, 2, 3]
    try:
        print(flatten([[1, 2], "ab"]))
    except TypeError as e:
        print("TypeError:", e)               # TypeError: ...
