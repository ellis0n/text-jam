def system(i):
    while True:
        i = i.upper()
        if i == "HELP":
            return helpme()
        elif i == "QUIT":
            print("bye!")
            exit()
        elif i == "SAVE":
            print("\nam i going to figure out how to implement this?")
            print("probably not\n")
        elif i == "BACK":
            return

        else:
            return


def helpme():
    print("\nHELP\n")
    print("type HELP to see this menu")
    print("type QUIT to exit the game")
    print("type BACK to return to the previous menu\n")
    return

