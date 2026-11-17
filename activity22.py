anime_type = [ "isakai", "action", "adventure", "comedy", "drama", "fantasy", "harem", "magic", "romance"]
anime_title = []

while True:
    ans = input("do you know any anime? (yes/no): ")

    if ans.lower() == "yes":
        print("what is its type --? select from the list")
        for x in anime_type:
            print(x)
        anime_type = input("type: ")

        title = input("what is its title? ")
        anime_title.append(title)
        continue
    else:
        print("thank you")
        break

              