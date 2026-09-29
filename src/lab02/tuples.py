"""ЛР2, задание C — записи студентов в виде кортежей."""

# Запись студента: (fio, group, gpa), например ("Иванов Иван Иванович", "BIVT-25", 4.6)
StudentRecord = tuple[str, str, float]


def format_record(rec: StudentRecord) -> str:
    
    fio, group, gpa = rec

    if not fio or not fio.strip():
        raise ValueError("ФИО не может быть пустым")

    if not group or not group.strip():
        raise ValueError("группа не может быть пуста")

    if not isinstance(gpa, (int, float)):
        raise TypeError(f"GPA должен быть числом, получен {type(gpa).__name__}")

    if gpa < 0.0 or gpa > 5.0:
        raise ValueError("GPA должен быть в диапазоне [0.0, 5.0]")

    words = fio.split()
    if len(words) < 2:
        raise ValueError("ФИО должно состоять из 2 или 3 слов")

    words = [w.capitalize() for w in words]

    surname = words[0]

    if len(words) == 2:
        initials = f"{words[1][0]}."
    elif len(words) == 3:
        initials = f"{words[1][0]}.{words[2][0]}."
    else:
        raise ValueError("ФИО должно состоять из 2 или 3 слов")

    return f"{surname} {initials}, гр. {group.strip()}, GPA {gpa:.2f}"


if __name__ == "__main__":
    print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
    print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
    print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
    print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))

    bad_records = [
        ("", "BIVT-25", 4.6),                 
        ("Иванов Иван", "", 4.6),             
        ("Иванов Иван", "BIVT-25", "4.6"),    
        ("Иванов Иван", "BIVT-25", 7.0),      
    ]
    for rec in bad_records:
        try:
            print(format_record(rec))
        except (ValueError, TypeError) as e:
            print(type(e).__name__ + ":", e)
