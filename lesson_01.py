def sub(a, b):
    """Вернуть разность a и b."""
    return a - b


def div(t, p):
    """Вернуть частное t и p. Если p == 0, вернуть None."""
    if p == 0:
        return None
    return t / p


def print_greeting():
    """Вывести приветствие."""
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

