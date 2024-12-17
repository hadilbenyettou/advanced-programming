numbers = [1, 2, 3, 4, 5]
bool = True
while bool:
    index = input("enter index : ")
    if not index.isdigit() and index != "-1":
        print("invalid input ,non-integer")
        continue
    else:
        index = int(index)
        if 0 <= index < len(numbers):
            value = input("enter new value")
            if not value.isdigit():
                print("value not valid not integer")
                continue
            else:
                value = int(value)
                numbers[index] = value
                print("new list :", numbers)
        elif index == -1:
            break
        else:
            print("index out of range !")
            continue
