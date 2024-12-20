numbers = [1, 2, 3, 4, 5]


def save_to_file(numbers):
    filename = input("Enter the filename to save the list: ")
    try:
        with open(filename, "w") as file:
            file.write(" ".join(map(str, numbers)))
        print(f"List saved to {filename}.")
    except Exception as e:
        print(f"Error saving the list: {e}")


def load_from_file():
    filename = input("Enter the filename to load the list: ")
    try:
        with open(filename, "r") as file:
            data = file.read().strip()
            return list(map(int, data.split()))
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Error: Invalid file format.")
    return None


while True:
    print("\ninitial list :", numbers)

    print(
        "\nMenu:\n\n1.Append\n2.insert\n3.Pop\n4.Remove\n5. Sort \n6. Reverse\n7. Search\n8. Save to a file\n9. Load a file\n10. Quit"
    )

    opt = input("Choose an option: ")

    if opt == "1":
        try:
            value = int(input("Enter value : "))
            numbers.append(value)
        except ValueError:
            print("Invalid input. Please enter an integer.")
    elif opt == "2":  # Insert
        try:
            value = int(input("Enter value : "))
            index = int(input("Enter index : "))
            if 0 <= index <= len(numbers):
                numbers.insert(index, value)
            else:
                print("Index out of range.")
        except ValueError:
            print("Invalid input. Please enter integers.")
    elif opt == "3":
        try:
            index = int(input("Enter index (default is last): ") or -1)
            if -len(numbers) <= index < len(numbers):
                removed = numbers.pop(index)
                print(f"Popped element: {removed}")
            else:
                print("Index out of range.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
        except IndexError:
            print("Cannot pop from an empty list.")
    elif opt == "4":
        try:
            value = int(input("Enter value to remove: "))
            numbers.remove(value)
        except ValueError:
            print("Value not found in the list or invalid input.")
    elif opt == "5":
        numbers.sort()
        print("List sorted.")
    elif opt == "6":
        numbers.reverse()
        print("List reversed.")
    elif opt == "7":
        try:
            value = int(input("Enter value to search for: "))
            if value in numbers:
                print(f"Value found at index {numbers.index(value)}.")
            else:
                print("Value not found in the list.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    elif opt == "8":
        save_to_file(numbers)
    elif opt == "9":
        loaded_list = load_from_file()
        if loaded_list is not None:
            numbers = loaded_list
            print("List loaded from file.")
    elif opt == "10":
        break
    else:
        print("Invalid opt. Please select a valid option.")
