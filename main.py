import vendors
from input import system as sys

print("\nfarmer's market manager simulator")

tables = 3
# Vendor pool
booked = {}

# Main menu

def mainmenu():
    print("\nmain menu\n")
    print("1: start game \n2: explain  \n3: quit ")
    choice = input("\n> ").lower()
    sys(choice)
    if choice == "1" or choice == "start" or choice == "one":
        game()
    elif choice == "2" or choice == "two" or choice == "e" or choice == "explain":
        print("\nyou are the manager of a farmer's market")
        print("\nyou need to keep the market running smoothly")
        print("\ntype HELP at any time to for a list of commands")
        mainmenu()
    elif choice == "3" or choice == "three" or choice == "q" or choice == "quit":
        exit()
    else:
        mainmenu()


# Start week cycle
def week(current):
    reference = {0: {
        "name": "sunday",
        "event": "none",
    }, 1: {
        "name": "monday",
        "event": "none",
    }, 2: {
        "name": "tuesday",
        "event": "none",
    }, 3: {
        "name": "wednesday",
        "event": "none",
    }, 4: {
        "name": "thursday",
        "event": "none",
    }, 5: {
        "name": "friday",
        "event": "none",
    }, 6: {
        "name": "saturday",
        "event": "none",
    }}

    name = reference[current]["name"]
    event = reference[current]["event"]

    for i in range(7):
        dayCycle(name, event)
        current += 1
        # market function
        if current == 6:
            print("Market day")
        if current == 7:
            break
        name = reference[current]["name"]
        event = reference[current]["event"]

    print("week over")


# Day cycle
def dayCycle(name, event):
    while True:
        print("\nits " + name + ".")
        print("what would you like to do?\n")
        print("1: view vendor database")
        print("2: view current bookings")
        print("3: book a vendor")
        print("4: wrap up for the day")
        choice = input("> ")
        sys(choice)
        if choice == "1":
            vendors.menu()
        elif choice == "2":
            vendors.booked()
        elif choice == "3":
            vendors.book()
        elif choice == "4":
            print("you wrapped up for the day.")
            break
        else:
            print("invalid selection")

# Game loop
def game():
    weeks = 1
    day = 1

    # Main loop
    while True:
        print("\nWEEK " + str(weeks))
        week(day)
        weeks += 1


mainmenu()
