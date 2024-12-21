def length(lst):
    if not isinstance(lst, list):
        print("It's not a list.")
        return None

    count = 0
    try:
        while True:
            _ = lst[count]
            count += 1
    except IndexError:
        pass
    return count


def mean(lst):
    if not lst:
        raise ValueError("Cannot calculate mean of an empty list.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("List must contain only numeric values.")
    return sum(lst) / len(lst)


def range_of_list(lst):
    if not lst:
        raise ValueError("Cannot calculate range of an empty list.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("List must contain only numeric values.")
    return max(lst) - min(lst)


numbers = [1, 18, 73, 44, 47]
print("Length:", length(numbers))
print("Mean:", mean(numbers))
print("Range:", range_of_list(numbers))


empty_list = []
print("Empty List - Length:", length(empty_list))  # Output: 0
try:
    print("Empty List - Mean:", mean(empty_list))
except ValueError as e:
    print(e)  # Error message

single_element = [42]
print("Single Element - Length:", length(single_element))  # Output: 1
print("Single Element - Mean:", mean(single_element))  # Output: 42.0
print("Single Element - Range:", range_of_list(single_element))  # Output: 0

negative_numbers = [-10, -20, -30]
print("Negative Numbers - Mean:", mean(negative_numbers))  # Output: -20.0
print("Negative Numbers - Range:", range_of_list(negative_numbers))  # Output: 20

floating_points = [1.5, 2.5, 3.5]
print("Floating Points - Mean:", mean(floating_points))  # Output: 2.5
print("Floating Points - Range:", range_of_list(floating_points))  # Output: 2.0

invalid_input = "Not a list"
