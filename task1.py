# Код по вычислениям длинный но с математикой плохо

def main():
    clent_second = int(input("Впишите время в секундах: "))
    day = clent_second // 86400
    hour = (clent_second % 86400) // (60 * 60)
    time = ((clent_second % 86400) % (60 * 60)) // 60
    second = (((clent_second % 86400) % (60 * 60)) % 60) % 60
    print(f"{day} дн : {hour} час : {time} мин : {second} сек")


if __name__ == "__main__":
    main()

#Фидбэк