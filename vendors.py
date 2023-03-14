from input import system as sys
# vendor menu

# simple vendor dictionary to get going
# create a class for vendors
vendors = {
    "1": {"name": "don's donuts",
          "owner": "don callahan",
          "category": "food",
          },
    "2": {"name": "brookside farms",
          "owner": "leah brookside",
          "category": "farm",
          },
    "3": {"name": "noobies",
          "owner": "emily van der noob",
          "category": "clothing",
          },
    "4": {"name": "sugar shack",
          "owner": "sarah martinez",
          "category": "food",
          },
    "5": {"name": "wood betwixt",
          "owner": "james wood",
          "category": "crafts",
          },
    "6": {"name": "the green grocer",
          "owner": "james green",
          "category": "farm",
          },
}

booked = {}


# Vendor menu
def menu():
    print("\nvendor menu\n")
    print("1: view vendors")
    print("2: edit vendor")
    print("3: add vendor")
    print("4: remove vendor")
    print("5: go back")

    while True:
        choice = input("\n> ")
        sys(choice)
        if choice == "1":
            list()
            menu()
        elif choice == "2":
            print("edit vendor\n")
            list()
            edit()
        elif choice == "3":
            print("add vendor\n")
            list()
            add()
        elif choice == "4":
            print("remove vendor\n")
            list()
            remove()
        elif choice == "5":
            return
        else:
            print("invalid choice")
            menu()


def list():
    print("\nvendor list")
    print("--------------------")
    for key in vendors:
        print(key + ": " + vendors[key]["name"])

# Edit vendor
def edit():
    print("\nedit vendor")
    selected = input("> ").upper()
    sys(selected)
    if selected == "help":
        print("type the number of the vendor you want to edit")
        print("type BACK to return to the vendor menu")
        edit()
    elif selected == "back":
        menu()
    # TODO: add a way to select a vendor by name
    elif selected not in vendors:
        print("invalid choice")
        edit()
    if selected in vendors:
        print("you selected:")
        print(vendors[selected]["name"])
        # Confirm selection
        confirm = input("confirm? (Y/N) ").upper()
        if confirm == "N":
            edit()
        # Edit submenu
        elif confirm == "Y":
            print("what would you like to edit?")
            print("1: name")
            print("2: owner")
            print("3: category")
            print("4: pick a different vendor")
            choice = input("> ")
            # Edit name
            if choice == "1" or choice == "name":
                print("current name: " + vendors[selected]["name"])
                print("new name: ")
                name = input("> ")
                vendors[selected]["name"] = name
                print("name changed to " + vendors[selected]["name"])
                menu()
            # Edit owner
            elif choice == "2" or choice == "owner":
                print("current owner: " + vendors[selected]["owner"])
                print("new owner: ")
                owner = input("> ")
                vendors[selected]["owner"] = owner
                print("owner changed to " + vendors[selected]["owner"])
                edit()
            # Edit category
            elif choice == "3" or choice == "category":
                print("current category: " + vendors[selected]["category"])
                print("new category: ")
                category = input("> ")
                vendors[selected]["category"] = category
                print("category changed to " + vendors[selected]["category"])
                edit()
            # Pick a different vendor
            elif choice.upper() == "4":
                edit()
            else:
                print("invalid selection")
                edit()
        else:
            print("invalid selection")
            edit()


# Add a vendor to the dictionary
def add():
    print("\nadd vendor")
    print("\nname: ")
    name = input("> ")
    print("\nowner: ")
    owner = input(">")
    print("\ncategory: \n")
    category = input(">")
    print("\nconfirm? (Y / N)")
    confirm = input("> ").upper()
    if confirm == "N":
        add()
    elif confirm == "Y":
        print("vendor added")
        vendors[len(vendors) + 1] = {"name": name, "owner": owner, "category": category}
        list()
        print("add another? (Y / N)")
        confirm = input("> ").upper()
        if confirm == "Y":
            add()
        elif confirm == "N":
            return
    else:
        print("invalid selection")
        add()
    menu()


# Remove a vendor from the dictionary
def remove():
    print("remove vendor\n")
    print("which vendor?")
    selected = input("> ")
    if selected == "HELP":
        print("type the number of the vendor you want to remove")
        print("type BACK to return to the vendor menu")
        remove()
    elif selected.upper() == "BACK":
        menu()
    elif selected not in vendors:
        print("invalid choice")
        remove()
    if selected in vendors:
        print("you selected:")
        print(vendors[selected]["name"])
        print("confirm? (Y / N)\n")
        confirm = input("> ").upper()
        if confirm == "N":
            remove()
        elif confirm == "Y":
            print("vendor removed")
            del vendors[selected]
            remove()
        else:
            print("invalid selection")
            remove()

def book():
    print("\nbook vendor")
    print("which vendor?")
    selected = input("\n> ")
    if selected.upper() == "HELP":
        print("type the number of the vendor you want to book")
        print("type BACK to return to previous menu")
        booked()
    elif selected.upper() == "BACK":
        return
    elif selected not in vendors:
        print("invalid choice")
        booked()
    if selected in vendors:
        print("you selected:")
        print(vendors[selected]["name"])
        confirm = input("confirm? (Y/N) ").upper()
        if confirm == "N":
            booked()
        elif confirm == "Y":
            print("vendor booked")
            booked[selected] = vendors[selected]
            book()
        else:
            print("invalid selection")
            booked()
        print("\nbook another? (y/n))")
        choice = input("> ")
        if choice == "y":
            book()
        elif choice == "n":

            return


def booked():
    print("\ncurrent bookings:\n")
    for i in booked:
        print(booked[i]["name"])

