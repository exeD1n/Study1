def main():
    """
    ГЛАВНОЕ ЗАДАНИЕ
    Отвечает за вывод списка кубов нечётных чисел
    """
    list_odd = []
    for number_power in range(0, 1001):
        number_odd = number_power ** 3
        if number_odd % 2 != 0:
            list_odd.append(number_odd)
    print(f"{list_odd} \n")

    """
    ЗАДАНИЕ под буквой А
    Отвечает за список не делимой суммы состовляющих числа на 7
    be - составляющие (название просто что бы потом вернуть нормальное число)
    """
    division_list = []
    for number in list_odd:
        be = number
        sum = 0
        while be != 0:
            sum = sum + be % 10
            be = be // 10
        if sum % 7 == 0:
            division_list.append(number)
    print(f"{division_list} \n")

    """
    ЗАДАНИЕ под буквой Б
    Отвечает за список к которому прибавлено 17 и делится на 7 без остатка
    """
    divisible_without = []
    for number in list_odd:
        numb = number
        numb += 17
        if numb % 7 == 0:
            divisible_without.append(number)
    print(f"{divisible_without}")


if __name__ == "__main__":
    main()

#Фидбэк