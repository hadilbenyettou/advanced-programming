people_rides = int(input("how many people need a ride?"))
people_fit = int(input("how many people can fit in one taxi?"))


taxis = people_rides // people_fit

if people_rides % people_fit != 0:
    taxis += 1

print("Number of taxis needed:", taxis)
