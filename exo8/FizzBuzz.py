number = int(input("Number: "))


def check_fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return None


result = check_fizzbuzz(number)
if result:
    print(result)
