cities = []

value = True
while value:
    city = input(
        "enter the name f the city or type stop to stop writing cities : "
    ).strip()
    if city == "stop":
        value = False
    population = len(city) * 1000000
    cities.append((city, population))

cities.sort(key=lambda x: x[1], reverse=True)
print("\nCities sorted by population:")
for city, population in cities:
    print(f"{city}: {population}")
