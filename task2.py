def main():
    """
    ГЛАВНОЕ ЗАДАНИЕ
    Отвечает за вывод списка кубов нечётных чисел от 1 до 1000
    то есть это числа 1, 3, 5, 7....
    """
    list_odd = []
    for number_power in range(0, 1001):
        if number_power%2 != 0:
            number = number_power**3
            list_odd.append(number)
    print(f"{list_odd} \n")

    """
    Задание 2А
    Вернуть список кубов нечётных чисел от 1 до 1000(сумма составляющих этого элемента делится на 7)
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
    Задание 2Б
    Вернуть список кубов нечётных чисел от 1 до 1000, прибавить по 17 к каждому эелементу (сумма составляющих этого элемента делится на 7)
    """
    divisible_without = []
    for number in list_odd:
        be = number
        be += 17
        sum = 0
        while be > 0:
            sum = sum + be % 10
            be = be // 10
        if sum%7 == 0:
            divisible_without.append(number)
    print(f"{divisible_without}")
    
if __name__ == "__main__":
    main()