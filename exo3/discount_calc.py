total_amount = int(input("Total amount:"))
nb_items = int(input("Number of items:"))
day_week = input("Day of week :")

weekdays = ["monday", "thusday", "wednesday", "thursday", "friday"]
weekends = ["Saturday", "Sunday"]
if day_week in weekdays:
    total_amount -= total_amount * 10 / 100
    if nb_items > 5:
        total_amount -= total_amount * 5 / 100
elif day_week in weekends:
    total_amount -= total_amount * 20 / 100
    if nb_items > 5:
        total_amount -= total_amount * 5 / 100
print("Total price after discount:", total_amount)
