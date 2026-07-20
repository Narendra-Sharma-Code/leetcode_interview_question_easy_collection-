def day_of_week(day):
    match day:
        case 1|2|3|4|5:
            print("It's Week Day")
        case 6|7:
            print("WOOO It's Weekend Babyy!!")
        case _:
            print("Invalid Day")
print(day_of_week(1))

