# python_labs

Лабораторные работы по программированию на Python.

Структура репозитория:

```
python_labs/
├─ README.md
├─ src/        # код по заданиям
│  └─ lab01/
└─ images/     # скриншоты работы программ
   └─ lab01/
```

Запуск любого задания из корня репозитория:

```bash
python src/lab01/01_greeting.py
```

---

# ЛР1 — Ввод/вывод и форматирование

## Задание 1 — Привет и возраст

Файл: [`src/lab01/01_greeting.py`](src/lab01/01_greeting.py)

```python
name = input("Имя: ")
age = int(input("Возраст: "))
print(f"Привет, {name}! Через год тебе будет {age + 1}.")
```

![Задание 1 — вывод приветствия и возраста через год](images/lab01/img01.png)

*Рис. 1. Работа программы `01_greeting.py`*

## Задание 2 — Сумма и среднее

Файл: [`src/lab01/02_sum_avg.py`](src/lab01/02_sum_avg.py)

```python
a = float(input("a: ").replace(",", "."))
b = float(input("b: ").replace(",", "."))
total = a + b
avg = total / 2
print(f"sum={total:.2f}; avg={avg:.2f}")
```

![Задание 2 — сумма и среднее двух чисел с 2 знаками](images/lab01/img02.png)

*Рис. 2. Работа программы `02_sum_avg.py`*

## Задание 3 — Чек: скидка и НДС

Файл: [`src/lab01/03_discount_vat.py`](src/lab01/03_discount_vat.py)

```python
price = float(input("price="))
discount = float(input("discount="))
vat = float(input("vat="))

base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

print(f"База после скидки: {base:.2f} ₽")
print(f"НДС:               {vat_amount:.2f} ₽")
print(f"Итого к оплате:    {total:.2f} ₽")
```

![Задание 3 — расчёт чека со скидкой и НДС](images/lab01/img03.png)

*Рис. 3. Работа программы `03_discount_vat.py`*

## Задание 4 — Минуты → ЧЧ:ММ

Файл: [`src/lab01/04_minutes_to_hhmm.py`](src/lab01/04_minutes_to_hhmm.py)

```python
m = int(input("Минуты: "))
hours = m // 60
minutes = m % 60
print(f"{hours}:{minutes:02d}")
```

![Задание 4 — перевод минут в формат ЧЧ:ММ](images/lab01/img04.png)

*Рис. 4. Работа программы `04_minutes_to_hhmm.py`*

## Задание 5 — Инициалы и длина строки

Файл: [`src/lab01/05_initials_and_len.py`](src/lab01/05_initials_and_len.py)

```python
fio = input("ФИО: ")
parts = fio.split()
initials = "".join(part[0].upper() for part in parts)
clean = " ".join(parts)
print(f"Инициалы: {initials}.")
print(f"Длина (символов): {len(clean)}")
```

![Задание 5 — инициалы и длина ФИО без лишних пробелов](images/lab01/img05.png)

*Рис. 5. Работа программы `05_initials_and_len.py`*

## Задание 6* — Подсчёт участников

Файл: [`src/lab01/06_count_participants.py`](src/lab01/06_count_participants.py)

```python
n = int(input())
full_time = 0
part_time = 0
for _ in range(n):
    surname, name, age, is_full_time = input().split()
    if is_full_time == "True":
        full_time += 1
    else:
        part_time += 1
print(full_time, part_time)
```

![Задание 6 — количество участников очно и заочно](images/lab01/img06.png)

*Рис. 6. Работа программы `06_count_participants.py`*

## Задание 7* — Расшифровка строки

Файл: [`src/lab01/07_decode_string.py`](src/lab01/07_decode_string.py)

Алгоритм: находим первую заглавную букву (начало строки), затем первую цифру после неё.
Символ сразу за цифрой — второй символ оригинала, отсюда получаем шаг. Дальше берём
символы с этим шагом, пока не встретим точку.

```python
s = input()

start = 0
while not s[start].isupper():
    start += 1

digit = start + 1
while not s[digit].isdigit():
    digit += 1
step = digit + 1 - start

result = ""
for i in range(start, len(s), step):
    result += s[i]
    if s[i] == ".":
        break
print(result)
```

![Задание 7 — расшифровка строки в Hello.](images/lab01/img07.png)

*Рис. 7. Работа программы `07_decode_string.py`*
