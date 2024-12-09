print("Runner 1:")
name1 = input("Name:")
time1 = float(input("Time (in seconds): "))

print("Runner 2:")
name2 = input("Name:")
time2 = float(input("Time (in seconds): "))

if time2 > time1:
    print("the faster runner is ", name1)
elif time1 > time2:
    print("the faster runner is ", name2)
else:
    print(name1, "and ", name2, "have the same time")
