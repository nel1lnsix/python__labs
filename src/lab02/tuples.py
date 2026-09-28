"""ЛР2, задание C — записи студентов в виде кортежей."""

# Запись студента: (fio, group, gpa), например ("Иванов Иван Иванович", "BIVT-25", 4.6)
StudentRecord = tuple[str, str, float]


def format_record(rec: StudentRecord) -> str:
    """Вернуть строку вида "Иванов И.И., гр. BIVT-25, GPA 4.60".

    - ФИО из 2 или 3 слов, лишние пробелы убираются,
      фамилия и инициалы с заглавной буквы.
    - GPA выводится с 2 знаками после точки, 0.0 <= GPA <= 5.0.

    Raises:
        ValueError: ...  (TODO: опиши, в каких случаях)
        TypeError: ...   (TODO: опиши, в каких случаях)
    """
    # TODO: твоё решение
    pass


if __name__ == "__main__":
    print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
    # Иванов И.И., гр. BIVT-25, GPA 4.60
    print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
    # Петров П., гр. IKBO-12, GPA 5.00
    print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
    # Петров П.П., гр. IKBO-12, GPA 5.00
    print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
    # Сидорова А.С., гр. ABB-01, GPA 4.00

    # Некорректные записи: должна быть ошибка
    bad_records = [
        ("", "BIVT-25", 4.6),                 # пустое ФИО
        ("Иванов Иван", "", 4.6),             # пустая группа
        ("Иванов Иван", "BIVT-25", "4.6"),    # GPA не число
        ("Иванов Иван", "BIVT-25", 7.0),      # GPA вне диапазона
    ]
    for rec in bad_records:
        try:
            print(format_record(rec))
        except (ValueError, TypeError) as e:
            print(type(e).__name__ + ":", e)
