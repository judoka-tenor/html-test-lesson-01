def funcA():
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
