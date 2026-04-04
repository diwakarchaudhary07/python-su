import random

def memory_game():
    items = ["🍎","🍌","🍇","🍎","🍌","🍇"]
    random.shuffle(items)
    revealed = ["?"] * len(items)

    while "?" in revealed:
        print(" ".join(revealed))
        first = int(input("Pick first index (0-5): "))
        second = int(input("Pick second index (0-5): "))

        if items[first] == items[second]:
            revealed[first] = items[first]
            revealed[second] = items[second]
            print("Match found!")
        else:
            print("Not a match!")

    print("🎉 You completed the puzzle!")

memory_game()
