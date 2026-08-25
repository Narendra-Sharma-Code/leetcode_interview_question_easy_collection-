def num(x):
    match x:
        case 1:
            print("one")
        case 2:
            print("two")
        case _:
            print("out of range")

num(4)