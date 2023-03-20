from Vendors import vendorpool, vendor

from Util.input import system as sys
from Util.gamestate import GameState
from Util.computer import Computer

print("\nfarmer's market manager simulator")


# Main menu
def main_menu():
    print("-" * 20)
    print("\nmain menu")
    print(("=" * 20) + "\n")

    print("1: start game \n2: the other option  \n3: quit ")
    choice = input("\n> ").lower()
    sys(choice)
    if choice == "1":
        game()
    elif choice == "2":
        print("\ni dont know what im doing! this is for text-jam 2023")
        print("i'll probably put something here later ")
        main_menu()
    elif choice == "3":
        exit()
    else:
        main_menu()


# Day cycle
def day_cycle(computer):
    while True:
        print("\nwhat do you do?\n")
        print("1. open myMarket \n2: use computer \n3: talk to the boss \n4: wrap up for the day")
        choice = input("\n> ")
        sys(choice)

        if choice == "1":
            computer.open_my_market()
        elif choice == "2":
            print("\nyou sit down at your computer. ")
            computer.run()
        elif choice == "3":
            print("\nyour boss is not here yet.")
        elif choice == "4":
            return
        else:
            print("invalid selection")

def day_one():
    print("\nwelcome to your new job!")
    print("you are the manager of a farmer's market")
    print("you need to keep the market running smoothly")
    print("you have five days to get ready for the first market day")
    print("use the myMarket app to prepare")
    print("you can also talk to your boss to get advice (soon)")
    print("type HELP any time to see a list of commands")
    print("good luck!\n")

    starter_vendors = vendorpool.VendorPool(5)
    starter_vendors.add_vendor(vendor.Vendor("bob", "bob's farm", "farmer"))
    starter_vendors.add_vendor(vendor.Vendor("sally", "sally's bakery", "craft"))
    starter_vendors.add_vendor(vendor.Vendor("joe", "ripple creek", "farmer"))
    starter_vendors.add_vendor(vendor.Vendor("sue", "sue's shwarma", "food"))
    starter_vendors.add_vendor(vendor.Vendor("donnie", "donnie's wooden wonders", "craft"))
    return starter_vendors

def market_day():
    print("\nmarket day!")
    # TODO: implement an actual fun gameplay mechanic LOL

# Game loop
def game():
    state = GameState(1, 1, vendorpool.VendorPool(5), vendorpool.VendorPool(0))
    computer = Computer(state)

    # Main loop
    while True:
        if state.day == 8:
            state.get_week_and_day()
            state.increment_week()
        elif state.day == 6:
            state.get_week_and_day()
            market_day()
            state.increment_day()
            day = state.day
        elif state.day == 7:
            print("\nweek: " + str(state.week) + " day: " + str(state.day))
            print("nothing happens on sunday. \n")
            state.increment_day()
        else:
            state.get_week_and_day()
            if state.day == 1 & state.week == 1:
                state.vendor_pool = day_one()
            day_cycle(computer)
            state.increment_day()


if __name__ == "__main__":
    main_menu()
