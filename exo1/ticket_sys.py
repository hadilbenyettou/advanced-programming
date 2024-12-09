name = input("please enter your name :")
if name == "VIP":
    print("enjoy the show for free")
else:
    nb = int(input("how many tickets you would like to buy:"))
    total_cost = nb * 15.5
    print("your total cost is ", total_cost)
    print("enjoy your teckets !")
