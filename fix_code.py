import os

files = {}

files["Lesson_fixed.py"] = '''my_name = "Антон"
my_name = "Антон Удовенко"
print(my_name)
'''

files["lesson1 -stack_fixed.py"] = '''def funcA():
    print("Начали выполнять А")
    funcB()
    print("Закончили выполнять А")


def funcB():
    print("Начали выполнять B")
    funcC()
    print("Закончили выполнять B")


def funcC():
    print("Начали выполнять C")
    print("Закончили выполнять C")


funcA()

my_heigh = 173
print(my_heigh)

my_name = "Антон"
my_name = "Антон Удовенко"
print(my_name)

pet_name = input("Киара ")


def print_letter(let):
    print(let, end="")


print_letter("C")
print_letter("т")
print_letter("у")
print_letter("д")
print_letter("е")
print_letter("н")
print_letter("т")
'''

files["lesson_1_task_2_fixed.py"] = '''my_age = "38"
print(my_age)
'''

files["lesson_1_task_3_fixed.py"] = '''first_name = "Антон"
last_name = "Удовенко"

print(f"Вас зовут: {last_name} {first_name}")

first_name = input("Введите имя: ")
last_name = input("Введите фамилию: ")

print(f"Вас зовут: {last_name} {first_name}")
'''

files["lesson_1_task_4_fixed.py"] = '''def print_greeting():
    print("Привет, мир!")


print_greeting()
'''

files["lesson_1_task_5_fixed.py"] = '''def print_num(num):
    print(num)


# Вызываем функцию 11 раз, передавая по одной цифре из номера
print_num(8)
print_num(8)
print_num(0)
print_num(0)
print_num(5)
print_num(5)
print_num(5)
print_num(3)
print_num(5)
print_num(3)
print_num(5)
'''

files["lesson_01_main_fixed.py"] = '''"""Модуль lesson_01: примеры функций и соблюдение PEP 8."""


def sub(a, b):
    """Вернуть разность двух чисел.

    :param a: Уменьшаемое.
    :param b: Вычитаемое.
    :return: Результат вычитания a - b.
    """
    return a - b


def div(t, p):
    """Вернуть частное двух чисел.

    Если делитель равен нулю, вернуть None.

    :param t: Делимое.
    :param p: Делитель.
    :return: Результат деления t / p или None при делении на ноль.
    """
    if p == 0:
        return None
    return t / p


def print_greeting():
    """Вывести стандартное приветствие на экран."""
    print("Привет, мир!")


def get_full_name():
    """Запросить имя и фамилию, вывести в формате Фамилия Имя."""
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    print(f"Вас зовут: {last_name} {first_name}")


if __name__ == "__main__":
    x = 15
    y = 7
    print(sub(x, y))
    print(div(x, y))
    print_greeting()
    get_full_name()
'''

for fname, content in files.items():
    os.system(f'attrib -r "{fname}"')
    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Записан: {fname}")

print("Все файлы записаны!")