numbers = []
shoe_sizes = []

numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)

numbers.append(1)
numbers.append(1)

numbers = list(set(numbers))

for val in [8, 9, 10, 11, 12]:
    shoe_sizes.append(val)


print("Numbers List: ", numbers)
print("Shoe Sizes List:", shoe_sizes)

list_comb = numbers + shoe_sizes

print("Combined list", list_comb)
