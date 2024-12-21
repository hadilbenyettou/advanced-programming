import statistics

user_list = []

while True:
    try:
        value = int(input("enter a number : "))
        if value == 0:
            break
        user_list.append(value)
        print("Current List:", user_list)
        print("Sorted List ascending order :", sorted(user_list))
        print("Sorted List descending order :", sorted(user_list, reverse=True))
    except ValueError:
        print("invalid value!")
# bonus

if user_list:
    print(f"Mean of the list : {statistics.mean(user_list):.2f}")
    print(f"Median of the list: {statistics.median(user_list):.2f}")

save_to_file = (
    input("Would you like to save the list to a file? (yes/no): ").strip().lower()
)
if save_to_file == "yes":
    filename = input("Enter the filename: ").strip()
    try:
        with open(filename, "w") as file:
            file.write("Current List : " + " ".join(map(str, user_list)) + "\n")
            file.write(
                "Sorted Numbers (Ascending order ): "
                + " ".join(map(str, sorted(user_list)))
                + "\n"
            )
            file.write(
                "Sorted Numbers (Descending order ): "
                + " ".join(map(str, sorted(user_list, reverse=True)))
                + "\n"
            )
            file.write(f"Mean: {statistics.mean(user_list):.2f}\n")
            file.write(f"Median: {statistics.median(user_list):.2f}\n")

    except Exception as e:
        print(f"Error saving to file: {e}")

print("\nProgram exited. Final list:", user_list)
