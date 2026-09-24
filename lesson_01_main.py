"Модуль lesson_01: примеры функций и соблюдение PEP 8."""


def sub(a, b):
    """Вернуть разность двух чисел.

    :param a: Уменьшаемое.
    :param b: Вычитаемое.
    :return: Результат вычитания a - b.
    """
    return a - b


def div(t, p):
    """Вернуть частное двух чисел. Если делитель равен нулю, вернуть None.

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
    """Запросить у пользователя имя и фамилию, затем вывести в формате «Фамилия Имя»."""
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
    