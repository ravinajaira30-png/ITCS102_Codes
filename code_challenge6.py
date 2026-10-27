size = int(input("input size: "))
edzil = 1
for x in range (size):
    for y in range (x):
        print(edzil, end=" ")
        edzil += 1
    print()