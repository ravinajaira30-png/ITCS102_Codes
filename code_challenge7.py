for x in range (4):
    for y in range (4):
        if x == 0 or y == 0 or x == 3 or y == 3:
            print("*", end=" ")
        else:
            print(" ", end=" ") 
    print()