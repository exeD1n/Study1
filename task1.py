def main():
    client_second = int(input("Впишите время в секундах: "))
    day = client_second // 86400
    hour = (client_second % 86400) // (60 * 60)
    time = ((client_second % 86400) % (60 * 60)) // 60
    second = (((client_second % 86400) % (60 * 60)) % 60) % 60
    
    if day == 0 and hour==0 and time == 0:
        print(f"{second} сек")
        
    elif day == 0 and hour==0:
        print(f"{time} мин : {second} сек")
        
    elif day == 0:
        print(f"{hour} час : {time} мин : {second} сек")
        
    else:
        print(f"{day} дн : {hour} час : {time} мин : {second} сек")
    
    
def for_in_main():
    client_second = str(input("Впишите несколько значений времи в секундах: "))
    array_time_client = [int(n) for n in client_second.split()]
    for first_time in array_time_client:
        day = first_time // 86400
        hour = (first_time % 86400) // (60 * 60)
        time = ((first_time % 86400) % (60 * 60)) // 60
        second = (((first_time % 86400) % (60 * 60)) % 60) % 60
        
        if day == 0 and hour==0 and time == 0:
            print(f"{second} сек")
        
        elif day == 0 and hour==0:
            print(f"{time} мин : {second} сек")

        elif day == 0:
            print(f"{hour} час : {time} мин : {second} сек")

        else:
            print(f"{day} дн : {hour} час : {time} мин : {second} сек")
        
        
if __name__ == "__main__":
    main()
    for_in_main()