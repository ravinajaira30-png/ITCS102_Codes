#jeepney simulator
route = ["Terminal", "Perez park", "pacific mall"]
passengers = []
SEATS = 6
FARE = 13
total = 0

while True:
    print()
    print("sakay:", passengers)
    print(len(passengers),"of", SEATS, "seats")
    print("1 Sakay 2 priority seat 3 para po!")
    print("4 baba sa pinto 5 baba sa harap")
    print("6 Seat check 7 balikan 8 exit")
    choice = input("choice: ")

    if choice == "1":
        if len(passengers) == SEATS:
            print("puno na!")
        else: 
            name = input("name: ")
            passengers.append(name)
            total = total + FARE
            print(name, "boarded at the back")

    elif choice == "2":
        if len(passengers) == SEATS: 
            print("puno na!")
        else:
            name= input("name: ")
            passengers.insert(0, name)
            total = total + FARE
            print(name, "took the priority seat.")

    elif choice == "3":
        name = input("who is getting off?")
        if name in passengers:
            passengers.remove(Name)
            print(name, "got off. takecare!")
        else:
            print(name, "is not on this jeep")

    elif choice == "4":
        if len(passengers) == 0:
            print("the jeep is empty")
        else:
            left =  passengers.pop()
            print(left, "got pff at the front")

    elif choice == "5":
        if len(passengers) == 0:
            print("jeep is empty")
        else:
            front = passengers.pop(0)
            print(front, "got off the front")

    elif choice == "6":
        for i in range(len(passengers)):
            print("seat", i + 1, passengers[i])

    elif choice == "7":
        route.reverse()
        print("route: ", route)