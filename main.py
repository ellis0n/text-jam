import vendor
import vendors
from input import system as sys
from gamestate import GameState
print("\nfarmer's market manager simulator")

# Main menu
def main_menu():
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
        main_menu()
    elif choice == "3" or choice == "three":
        exit()
    else:
        main_menu()



# Day cycle
def day_cycle():
    while True:
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
            return
        else:
            print("invalid selection")

# Game loop
def game():
    state = GameState(1, 1, vendor.VendorPool(10), vendor.VendorPool(5))
    week = state.week
    day = state.day
    vendor_pool = state.vendor_pool
    booked_pool = state.booked

    print(day)
    print(week)
    # print(vendor_pool)
    # print(booked_pool)

    # Initialize vendors

    def market_day():
        print("market day!")
        print("code goes here \n")
        input("press enter to continue \n")


    def day_off():
        print("day off!")
        print("code goes here \n")
        input("press enter to continue \n")

    # Main loop
    # Main loop
    while True:
        if day == 8:
            state.increment_week()
            week = state.week
            day = 1
        elif day == 6:
            print("\nweek: " + str(week) + " day: " + str(day))
            market_day()
            state.increment_day()
            day = state.day
        elif day == 7:
            print("\nweek: " + str(week) + " day: " + str(day))
            day_off()
            state.increment_day()
            day = state.day
        else:
            print("week: " + str(week) + " day: " + str(day))
            day_cycle()
            state.increment_day()
            day = state.day

main_menu()
