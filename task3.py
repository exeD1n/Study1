# Склонение слова ПАДЕЖ до 20 можно упростить с помощью библиотеки

def main():
    massiv_padej = ["процент", "процента", "процентов"]
    client_ch = input("Введите число от 1 до 100: ")

    if client_ch[-1] == '1':
        print(client_ch, massiv_padej[0])

    elif client_ch[-1] in ('2', '3', '4'):
        print(client_ch, massiv_padej[1])

    else:
        print(client_ch, massiv_padej[2])


if __name__ == "__main__":
    main()

#Фидбэк