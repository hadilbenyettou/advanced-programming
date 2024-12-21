def get_positive_integer():
    while True:
        try:
            N = int(input("Please enter a positive integer: "))
            if N > 0:
                return N
            else:
                print("The number must be positive. Try again.")
        except ValueError:
            print("Invalid input! Please enter an integer.")


N = get_positive_integer()


for num in range(-N, N + 1):
    if num != 0:
        print(num)
