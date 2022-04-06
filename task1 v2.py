# Изначально было написано
# Второй вариант в файле zadanie.py
import datetime


def main():
    duration = int(input("Введите время в секундах: "))
    time_format = str(datetime.timedelta(seconds=duration))
    print(time_format)


if __name__ == "__main__":
    main()


#Фидбэк