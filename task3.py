# Склонение слова [процент] до 100

def main():
    while True:
        massiv_padej = ["процент", "процента", "процентов"]
        client_ch = int(input("Введите число от 1 до 100: "))
    
        second_digit = client_ch % 10
        
        exception = {11, 12, 13, 14}
        
        if client_ch in exception:
            print(client_ch, massiv_padej[2])
    
        elif second_digit in (2, 3, 4):
            print(client_ch, massiv_padej[1])
            
        elif second_digit == 1:
            print(client_ch, massiv_padej[0])
            
        else:
            print(client_ch, massiv_padej[2])

if __name__ == "__main__":
    main()